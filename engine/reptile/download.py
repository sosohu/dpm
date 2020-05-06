#!/usr/bin/env python
# encoding:utf-8

import sys

sys.path.insert(0, "C:\\work\\dpm")

from engine.common.curl.get_request import CGetRequest

def main():
    lGetRequest = CGetRequest('dpm get')
    lGetRequest.putUrl('https://digicol.dpm.org.cn/cultural/queryList')

    lParams = {}
    lParams['page'] = 1
    lParams['authorizeStatus'] = 'false'
    lParams['hasImage'] = 'false'
    lParams['cateList'] = 17
    lParams['ranNum'] = 0
    lGetRequest.putParams(lParams)
    lGetRequest.putHeader(['Referer : https://digicol.dpm.org.cn/list?page=1&category=17'])
    lResult = lGetRequest.performRequest()
    print(lResult)
    del lGetRequest

if __name__ == "__main__":
    main()