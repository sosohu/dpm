#!/usr/bin/env python
# encoding:utf-8

import json
import re

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
        gLogger.info("Start to download category {} page {}.".format(self.__mCategory, self.__mPage))
        self.__getResouce()
        gLogger.info("Download category {} page {} finished.".format(self.__mCategory, self.__mPage))
        return

    def __getResouce(self):
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
                        gLogger.error("Resource metadata info in page {} is not correct. Row data: {}.".format(self.__mPage, lRowData))
                        continue

                    if gMetadataDpm.isExistedResource(lUuid):
                        gLogger.warn("Resource {} in page {} has been existed. Skip it".format(lUuid, self.__mPage))
                        continue

                    lResourceName = lRowData["name"] or "None"
                    lResourceDynastyName = lRowData["dynastyName"] or "None"

                    gLogger.debug("Start to process {} {}".format(lResourceName, lResourceDynastyName))

                    if lRowData["bigImage"]:
                        #lGetRequest.cleanData()
                        lGetRequest.putUrl(gConfigFileWrapper.getStr('dpm', 'image_source_url').format(lRowData["bigImage"]))
                        lGetRequest.putHeader([self.__Referer])

                        lResponseCode = lGetRequest.performRequest()

                        if lResponseCode == 200:
                            lResponseHeader = lGetRequest.getResponseHeader()
                            if 'image/jpeg' in lResponseHeader['content-type']:
                                lResponsebody = lGetRequest.getResponseBody()
                                lOutputFile = "{}/{}-{}-{}.jpg".format(self.__mSavePath, lResourceDynastyName, lResourceName, lUuid)
                                lOutputFile = re.sub(r'[*?"<>|]', '', lOutputFile)
                                with open(lOutputFile, 'wb+') as out_file:
                                    out_file.write(lResponsebody)
                                    # Write metadata to database
                                    lRowData["page"] = self.__mPage
                                    gMetadataDpm.insertResource(lUuid, lRowData)
                            else:
                                gLogger.error("Fetch resource {}-{} in page {} failed. Response header: {}".format(lResourceDynastyName, lResourceName, self.__mPage,lResponseHeader))
                        else:
                            gLogger.error("Fetch resource {}-{} in page {} failed. Response code: {}.".format(lResourceDynastyName, lResourceName, self.__mPage, lResponseCode))
                    else:
                        gLogger.warn("The resource {}-{} in page {} does not have the big image".format(lResourceDynastyName, lResourceName, self.__mPage))

                del lGetRequest
            else:
                gLogger.warn("The page {}'s dpm list return result is not expected. Response body: {}".format(self.__mPage, lResponsebody))
        else:
            gLogger.error("Fetch page {}'s dpm list failed. Response code: {}. Response header: {}".format(self.__mPage, lResponseCode, lResponseHeader))

        del lPostRequest

def downloadDpmRun(iCategory, iPage, iSavePath):
    lDownloadDpm = CDownloadDpm(iCategory, iPage, iSavePath)
    lDownloadDpm.run()