#!/usr/bin/env python
# coding:utf-8
"""
  Author:  lianjun.yao --<>
  Created: 2017/3/6
"""
from PyQt4.QtCore import QThread, pyqtSignal
from  MqJsonFun import *

import os,time,logging
logger_workthread = logging.getLogger('workthread')   

class workThread(QThread):
    """工作线程"""
    sinOut1 = pyqtSignal(str)
    sinOut2 = pyqtSignal(int)
    # ----------------------------------------------------------------------
    def __init__(self, parent=None):
        """初始化"""
        super(workThread, self).__init__(parent)
        self.filePath = ''
        self.modelVhost = ''
        self.addVhost = ''
        self.labelList = []
    
    def setup(self, JsonPath, labelList, modelVhost, newVhost):
        if not  os.path.exists(JsonPath):
            self.sinOut1.emit(u'输入的Json文件地址有误，请检查')
            return False        
        self.labelList = labelList
        if  len(labelList) <= 0:
            self.sinOut1.emit(u'配置文件中需要修改的label未进行配置，请修改配置文件')
            return False
        self.filePath = JsonPath
        if modelVhost == '':
            self.sinOut1.emit(u'输入的模板Vhost为空，请重新输入')
            return False
        self.modelVhost = modelVhost
        self.addVhost = newVhost
        return True
    
        
        
    def work(self):
        try:
            jsonDic = turnJson2Dic(self.filePath)
            if not jsonDic:
                self.sinOut1.emit(u'将JSON转换为DIC失败')
                return False
            for label in self.labelList:
                ret, jsonDic = addJson(jsonDic, label, self.modelVhost, self.addVhost)
                if ret:
                    self.sinOut1.emit(u'修改标签 %s，新增 %s'%(label,self.addVhost))    
                else:
                    self.sinOut1.emit(u'未修改标签 %s'%label)
            
            strtime = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time()))
            newJsonPath = os.path.split(self.filePath)[0] + r'/' + strtime + r'.json'
            ret = turnDic2Json(jsonDic, newJsonPath)
            if not ret :
                self.sinOut1.emit(u'生成json文件失败')
                return False
            self.sinOut1.emit(u'生成Json文件，路径：%s'%newJsonPath)
            return True
        except Exception,e:
            logger_workthread.exception(str(e))
            self.sinOut1.emit(u'发生异常，请查看日志')
            return False
        
    def run(self):
        try:
            self.sinOut2.emit(False)
            ret = self.work()
            if ret:
                self.sinOut1.emit(u'执行成功 ^_^')
            else:
                self.sinOut1.emit(u'执行失败 T.T')                            
        except Exception,e:
            print e
        self.sinOut2.emit(True)