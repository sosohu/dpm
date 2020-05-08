#!/usr/bin/env python
# encoding:utf-8

import sys
import json

sys.path.insert(0, "C:\\work\\dpm")

from engine.common.curl.get_request import CGetRequest
from engine.common.curl.post_request import CPostRequest
from engine.common.start_up import gLogger


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
    lResponseCode = lPostRequest.performRequest()
    lResponseHeader = lPostRequest.getResponseHeader()
    if lResponseCode == 200 and 'text/plain' in lResponseHeader['content-type']:
        lResponsebody = lPostRequest.getResponseBody()
        lResult = json.loads(lResponsebody.decode('utf-8'))

        if lResult and lResult["rows"] and len(lResult["rows"]) > 0:
            lRowData = lResult["rows"][0]
            gLogger.debug("Start to process {} {} {}".format(lRowData["name"], lRowData["dynastyName"], lRowData["bigImage"]))

            if lRowData["bigImage"]:
                lGetRequest = CGetRequest('dpm detail get')
                lGetRequest.putUrl("https://shuziwenwu-1259446244.cos.ap-beijing.myqcloud.com{}".format(lRowData["bigImage"]))
                lGetRequest.putHeader(['Referer:https://digicol.dpm.org.cn/list?page=1&category=17'])

                lResponseCode = lGetRequest.performRequest()
                lResponseHeader = lGetRequest.getResponseHeader()
                if lResponseCode == 200 and 'image/jpeg' in lResponseHeader['content-type']:
                    lResponsebody = lGetRequest.getResponseBody()
                    with open('out.jpg', 'wb') as out_file:
                        out_file.write(lResponsebody)
                
                del lGetRequest

        del lPostRequest

# with open('out.jpg', 'wb') as out_file:
#     out_file.write(lResponsebody)
#gLogger.debug("Get request return data: {}".format(lResponseHeader))

#print(self._mResponseHeader["content-type"])
#lResponsebody = self._mResponseData.getvalue()
#return json.loads(lResponsebody.decode('utf-8'))

if __name__ == "__main__":
    main()

