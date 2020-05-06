#!/usr/bin/env python
# encoding:utf-8

import time
import inspect
from engine.common.enum import *
from datetime import date, datetime

def gNowTimeFunc():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

def gStr2BooleanFunc(iStr):
    return iStr.lower() in ['true', '1', 'yes']

def gNowTimeStampFunc():
    return int(time.time())

def gFaiedFunc(iCode):
    return iCode != EnumErrorCode.S_OK

def gGetTodayTimeStampFunc():
    lTime = time.strftime("%Y-%m-%d 00:00:00", time.localtime())
    return int(time.mktime(datetime.strptime(lTime, "%Y-%m-%d %H:%M:%S").timetuple()))

def gGetDiffDaysFunc(iBeginTime, iEndTime):
    if iBeginTime >= iEndTime:
        return 0
        
    return int((iEndTime - iBeginTime) / (24 * 60 * 60))