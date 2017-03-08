# -*- coding: utf-8 -*-

"""
  Author:  lianjun.yao --<>
  Created: 2017/3/6
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from WorkThread import workThread
from Ui_MqJsonEdit import Ui_MqJsonEdit

import logging 
import logging.config
LOG_FILE = 'tst.log'
#输出到屏幕   
ch = logging.StreamHandler() 
#写入文件实例化
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler 
fmt = '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)   # 实例化formatter
handler.setFormatter(formatter)      # 为handler添加formatter
logger_main = logging.getLogger('main')    # 获取名为tst的logger
logger_main.addHandler(handler)           # 为logger添加handler
#logger_main.addHandler(ch)
logger_main.setLevel(logging.DEBUG)


from  config import *

class MqJsonEdit(QMainWindow, Ui_MqJsonEdit):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QTextCodec.setCodecForCStrings(QTextCodec.codecForName('gbk'))
    
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.work = workThread()
        self.work.sinOut1.connect(self.printLog)
        self.work.sinOut2.connect(self.enableButtonStatus)        
        try:
            modelVhost = getConfig('modelVhost')
            self.lineEdit_modelVhost.setText(modelVhost)
            filePath = getTemp('JsonPath')
            self.lineEdit_filePath.setText(filePath)
        except Exception,e:
            logger_main.exception(str(e))

    @pyqtSignature("")
    def on_toolButton_clicked(self):
        """
        选择json路径
        """
        filePath = self.lineEdit_filePath.text()
        filePath = unicode(filePath,'gbk')
        if filePath.strip() == '':
            lastPath = QString()
        else:
            lastPath = filePath
        sousePath = QFileDialog.getOpenFileName(self, self.tr('Open Json'), lastPath,
                                        self.tr("json Files(*.json)"))
        if sousePath =="" :
            return
        self.lineEdit_filePath.setText(sousePath)
        saveTemp("JsonPath",sousePath)
        
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        filePath = self.lineEdit_filePath.text()
        filePath = unicode(filePath,'gbk')    
        labelstr = getConfig('editLabel')
        labelList = labelstr.split(',')
        modelVhost = self.lineEdit_modelVhost.text()
        modelVhost = str(modelVhost)
        newVhost = self.lineEdit_newVhost.text()
        newVhost = str(newVhost)          
        ret = self.work.setup(filePath,labelList,modelVhost,newVhost)
        if not ret:
            return False
        self.work.start()
        
        
    def printLog(self,strWords):
        try:
            strWords = unicode(strWords)
        except:
            pass 
        self.textEdit_logShow.append(strWords)
        logger_main.info(strWords)
        
    def enableButtonStatus(self,bstatus):
        bstatus = bool(bstatus)
        self.pushButton.setEnabled(bstatus)
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MqJsonEdit = MqJsonEdit()
    MqJsonEdit.show()
    sys.exit(app.exec_())
    