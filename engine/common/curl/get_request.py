#!/usr/bin/env python
# encoding:utf-8

import urllib.parse
import pycurl
import json
import shutil
import io
from PIL import Image
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
        if not type(iHeader) is list:
            gLogger.error("Expect a list but input type is: {}".format(type(iHeader)))
            return

        self.__mHeader = iHeader

    def putUrl(self, iUrl):
        self.__mUrl = iUrl

    def putParams(self, iParams):
        if not type(iParams) is dict:
            gLogger.error("Expect a dict but input type is: {}".format(type(iParams)))
            return
        
        self.__mParams = urllib.parse.urlencode(iParams)

    def performRequest(self):
        gLogger.debug("Start to raise a get request. Url: {}. Params: {}. Header: {}".format(self.__mUrl, self.__mParams or "", self.__mHeader))

        if self.__mParams:
            self._mCurl.setopt(pycurl.URL, self.__mUrl + '?' + self.__mParams)
        else:
            self._mCurl.setopt(pycurl.URL, self.__mUrl)
        
        self._mCurl.setopt(pycurl.HTTPHEADER, self.__mHeader)
        
        return CBaseRequest._performRequest(self)