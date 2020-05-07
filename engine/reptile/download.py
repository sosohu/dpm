#!/usr/bin/env python
# encoding:utf-8

import sys

sys.path.insert(0, "C:\\work\\dpm")

from engine.common.curl.get_request import CGetRequest
from engine.common.curl.post_request import CPostRequest

def main():
    lPostRequest = CPostRequest('dpm list post')
    lPostRequest.putUrl('https://digicol.dpm.org.cn/cultural/queryList')

    lFields = {}
    lFields['page'] = 1
    lFields['authorizeStatus'] = 'false'
    lFields['hasImage'] = 'false'
    lFields['cateList'] = 17
    lFields['ranNum'] = 0
    lPostRequest.putFields(lFields)
    lPostRequest.putHeader(['Referer:https://digicol.dpm.org.cn/list?page=1&category=17'])
    lResult = lPostRequest.performRequest()
    #print(lResult)
    if lResult and lResult["rows"] and len(lResult["rows"]) > 0:
        lRowData = lResult["rows"][0]
        print(lRowData["name"], lRowData["dynastyName"], lRowData["bigImage"])

        if lRowData["bigImage"]:
            lGetRequest = CGetRequest('dpm detail get')
            lGetRequest.putUrl("https://shuziwenwu-1259446244.cos.ap-beijing.myqcloud.com{}".format(lRowData["bigImage"]))
            lGetRequest.putHeader(['Referer:https://digicol.dpm.org.cn/list?page=1&category=17'])
            lImage = lGetRequest.performRequest()

    del lPostRequest

if __name__ == "__main__":
    main()