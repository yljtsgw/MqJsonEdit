# -*- coding: utf-8 -*-
"""
  Author:  lianjun.yao --<>
  Created: 2017/3/6
"""
import json,copy,os

def addJson(pJsonDic, label, modelVhost, newVhost, vhost = 'vhost'):
    if not pJsonDic.has_key(label):
        print "There is no %s in Json"%label
        return False,pJsonDic
    labelList = []
    newmodelList = []
    newLabelList = []
    addLabelList = []
    labelList = pJsonDic[label]
    for labelDic in labelList:
        if not labelDic.has_key(vhost):
            continue
        if labelDic[vhost] ==  str(newVhost):
            labelList.remove(labelDic)
        if labelDic[vhost] ==  str(modelVhost):
            modelDic = copy.deepcopy(labelDic)
            modelDic[vhost] = newVhost
            addLabelList.append(modelDic)
    newLabelList = labelList + addLabelList
    pJsonDic[label] = newLabelList
    return True,pJsonDic


def turnJson2Dic(pJsonPath):
    try:
        with open(pJsonPath,'r') as f:
            jsonDic = json.load(f)        
        return jsonDic
    except Exception,e:
        print e
        return False
    
def turnDic2Json(Dic,pJsonPath):
    try:
        
        if len(Dic) != 0 :
            with open(pJsonPath,'w') as f:
                json.dump(Dic,f)
            return True
    except Exception,e:
        print e
        return False