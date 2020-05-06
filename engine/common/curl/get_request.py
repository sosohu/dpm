#!/usr/bin/env python
# encoding:utf-8

import urllib.parse
import pycurl
import json
from engine.common.curl.base_request import CBaseRequest
from engine.common.start_up import gLogger

class CGetRequest(CBaseRequest):
    def __init__(self, iName):
        CBaseRequest.__init__(self, iName)
        self.__mUrl = None
        self.__mParams = None
        self.__mHeader = []

    def __del__(self):
        CBaseRequest.__del__(self)

    def putHeader(self, iHeader):
        self.__mHeader = iHeader

    def putUrl(self, iUrl):
        self.__mUrl = iUrl

    def putParams(self, iParams):
        self.__mParams = iParams

    def performRequest(self):
        gLogger.debug("Start to raise a get request. Url: {}. Params: {}. Header: {}".format(self.__mUrl, urllib.parse.urlencode(self.__mParams), self.__mHeader))

        self._mCurl.setopt(pycurl.URL, self.__mUrl + '?' + urllib.parse.urlencode(self.__mParams))
        self._mCurl.setopt(pycurl.HTTPHEADER, self.__mHeader)
        self._mCurl.perform()
        # Get the content stored in the BytesIO object (in byte characters) 
        lResponsebody = self._mResponseData.getvalue()
        # Decode the bytes stored in get_body to HTML and print the result 
        print(lResponsebody)
        return json.loads(lResponsebody.decode('utf-8'))