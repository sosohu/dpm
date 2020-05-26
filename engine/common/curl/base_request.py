#!/usr/bin/env python
# encoding:utf-8

from io import BytesIO
import pycurl
from engine.common.start_up import gConfigFileWrapper
from engine.common.start_up import gLogger

class CBaseRequest():
    def __init__(self, iName):
        self._mCurl = None
        self.__ResponseCode = None
        self.__initMember(iName)
        self.__constructCurl()

    def __del__(self):
        if self._mCurl:
            self._mCurl.close()

    def __cleanData__(self):
        self.__ResponseCode = None
        self._mResponseHeaderByte = BytesIO()
        self._mResponseDataByte = BytesIO()
        self._mCurl.setopt(pycurl.WRITEHEADER, self._mResponseHeaderByte)
        self._mCurl.setopt(pycurl.WRITEDATA, self._mResponseDataByte)

    def __initMember(self, iName):
        self._mName = iName
        #self.__mCookieFile  =  "{}-{}-{}.cookie".format(iName, gNowTimeFunc(), uuid.uuid4())
        self.__mCookieFile = "{}{}.cookie".format(gConfigFileWrapper.getStr('curl', 'cookie_folder'), self._mName)
        self._mResponseHeaderByte = BytesIO()
        self._mResponseDataByte = BytesIO()
        self._mResponseHeader = {}
        self._mResponseData = {}

    def __constructCurl(self):
        self._mCurl = pycurl.Curl()
        self._mCurl.setopt(pycurl.VERBOSE, gConfigFileWrapper.getBoolean('curl', 'verbose'))
        self._mCurl.setopt(pycurl.CONNECTTIMEOUT, gConfigFileWrapper.getInt('curl', 'connect_timeout'))
        self._mCurl.setopt(pycurl.TIMEOUT, gConfigFileWrapper.getInt('curl', 'timeout'))
        self._mCurl.setopt(pycurl.USERAGENT, gConfigFileWrapper.getStr('curl', 'user_agent'))
        self._mCurl.setopt(pycurl.WRITEHEADER, self._mResponseHeaderByte)
        self._mCurl.setopt(pycurl.WRITEDATA, self._mResponseDataByte)
        self._mCurl.setopt(pycurl.COOKIEJAR, self.__mCookieFile)
        self._mCurl.setopt(pycurl.COOKIEFILE, self.__mCookieFile)
        self._mCurl.setopt(pycurl.SSL_VERIFYPEER, 0)
        self._mCurl.setopt(pycurl.SSL_VERIFYHOST, 0)

    def _performRequest(self):
        try:
            self._mCurl.perform()
        except pycurl.error:
            return -1

        self._washHeader()
        self._mResponseData =  self._mResponseDataByte.getvalue()

        gLogger.debug("HTTP request return code: {}".format(self.__ResponseCode))
        return self.__ResponseCode

    def _washHeader(self):
        gLogger.debug("HTTP request return header: {}".format(self._mResponseHeaderByte.getvalue().decode('utf-8')))
        lHeaderList = self._mResponseHeaderByte.getvalue().decode('utf-8').split('\n')

        self._mResponseHeader = {}

        for lField in lHeaderList:
            if ':' not in lField:
                if 'HTTP' in lField:
                    self.__ResponseCode = lField.split(' ', 2)[1]
                    self.__ResponseCode = int(self.__ResponseCode)
                continue

            lName, lValue = lField.split(':', 1)

            lName = lName.strip()
            lValue = lValue.strip()
            lName = lName.lower()

            self._mResponseHeader[lName] = lValue

    def getResponseHeader(self):
        return self._mResponseHeader

    def getResponseBody(self):
        return self._mResponseData