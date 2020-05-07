#!/usr/bin/env python
# encoding:utf-8

import urllib.parse
import pycurl
import json
from engine.common.curl.base_request import CBaseRequest
from engine.common.start_up import gLogger

class CPostRequest(CBaseRequest):
    def __init__(self, iName):
        CBaseRequest.__init__(self, iName)
        self.__mUrl = None
        self.__mFields = None
        self.__mHeader = []

    def __del__(self):
        CBaseRequest.__del__(self)

    def putHeader(self, iHeader):
        if not type(iHeader) is list:
            gLogger.error("Expect a list but input type is: {}".format(type(iHeader)))
            return

        self.__mHeader = iHeader

    def putUrl(self, iUrl):
        self.__mUrl = iUrl

    def putFields(self, iFields):
        if not type(iFields) is dict:
            gLogger.error("Expect a dict but input type is: {}".format(type(iFields)))
            return

        self.__mFields = urllib.parse.urlencode(iFields)

    def performRequest(self):
        gLogger.debug("Start to raise a post request. Url: {}. Fields: {}. Header: {}".format(self.__mUrl, self.__mFields, self.__mHeader))

        self._mCurl.setopt(pycurl.URL, self.__mUrl)
        self._mCurl.setopt(pycurl.HTTPHEADER, self.__mHeader)
        self._mCurl.setopt(pycurl.POSTFIELDS, self.__mFields)
        self._mCurl.perform()
        # Get the content stored in the BytesIO object (in byte characters) 
        lResponsebody = self._mResponseData.getvalue()
        # Decode the bytes stored in get_body to HTML and print the result 
        gLogger.debug("Post request return data: {}".format(lResponsebody.decode('utf-8')))
        return json.loads(lResponsebody.decode('utf-8'))