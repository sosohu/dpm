#!/usr/bin/env python
# encoding:utf-8

import json

from engine.common.start_up import gConfigFileWrapper
from engine.common.start_up import gLogger
from engine.common.curl.get_request import CGetRequest
from engine.common.curl.post_request import CPostRequest
from engine.reptile.metadata_dpm import gMetadataDpm

class CDownloadDpm():
    def __init__(self, iCategory, iPage, iSavePath):
        self.__mCategory = iCategory
        self.__mPage = iPage
        self.__mSavePath = iSavePath
        self.__Referer = gConfigFileWrapper.getStr('dpm', 'query_list_referer').format(self.__mPage, self.__mCategory)

    def __del__(self):
        return

    def run(self):
        return

    def __getMetadata(self):
        lPostRequest = CPostRequest('download dpm list post')
        lPostRequest.putUrl(gConfigFileWrapper.getStr('dpm', 'query_list_url'))

        lFields = {}
        lFields['page'] = self.__mPage
        lFields['authorizeStatus'] = 'false'
        lFields['hasImage'] = 'false'
        lFields['cateList'] = self.__mCategory
        lFields['ranNum'] = 0
        lPostRequest.putFields(lFields)
        lPostRequest.putHeader([self.__Referer])

        lResponseCode = lPostRequest.performRequest()

        lResponseHeader = lPostRequest.getResponseHeader()
        if lResponseCode == 200 and 'text/plain' in lResponseHeader['content-type']:
            lResponsebody = lPostRequest.getResponseBody()
            lResult = json.loads(lResponsebody.decode('utf-8'))

            if lResult and lResult["rows"] and len(lResult["rows"]) > 0:
                lRowsData = lResult["rows"]

                lGetRequest = CGetRequest('dpm detail get')
                for lRowData in lRowsData:
                    lUuid = lRowData["uuid"]
                    if not lUuid:
                        gLogger.error("Resource metadata info is not correct. Row data: {}.".format(lRowData))
                        continue

                    if gMetadataDpm.isExistedResource(lUuid):
                        gLogger.warn("Resource {} has been existed. Skip it".format(lUuid))
                        continue

                    lResourceName = lRowData["name"] or "None"
                    lResourceDynastyName = lRowData["dynastyName"] or "None"

                    gLogger.debug("Start to process {} {}".format(lResourceName, lResourceDynastyName))

                    if lRowData["bigImage"]:
                        lGetRequest.putUrl(gConfigFileWrapper.getStr('dpm', 'image_source_url').format(lRowData["bigImage"]))
                        lGetRequest.putHeader([self.__Referer])

                        lResponseCode = lGetRequest.performRequest()
                        lResponseHeader = lGetRequest.getResponseHeader()

                        if lResponseCode == 200 and 'image/jpeg' in lResponseHeader['content-type']:
                            lResponsebody = lGetRequest.getResponseBody()
                            lOutputFile = "{}/{}-{}.jpg".format(self.__mSavePath, lResourceDynastyName, lResourceName)
                            with open(lOutputFile, 'wb') as out_file:
                                out_file.write(lResponsebody)
                        else:
                            gLogger.error("Fetch resource {}-{} failed. Response code: {}.".format(lResourceDynastyName, lResourceName, lResponseCode))

                        # Write metadata to database
                        gMetadataDpm.insertResource(lUuid, lRowData)

                    else:
                        gLogger.warn("The resource {}-{} does not have the big image".format(lResourceDynastyName, lResourceName))

                        
                del lGetRequest
            else:
                gLogger.warn("The dpm list return result is not expected. Response body: {}".format(lResponsebody))
        else:
            gLogger.error("Fetch dpm list failed. Response code: {}. Response header: {}".format(lResponseCode, lResponseHeader))

        del lPostRequest