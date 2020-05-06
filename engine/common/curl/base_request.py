#!/usr/bin/env python
# encoding:utf-8

from io import BytesIO
import pycurl
from engine.common.start_up import gConfigFileWrapper

class CBaseRequest():
    def __init__(self, iName):
        self._mCurl = None
        self.__initMember(iName)
        self.__constructCurl()

    def __del__(self):
        if self._mCurl:
            self._mCurl.close()

    def __initMember(self, iName):
        self._mName = iName
        #self.__mCookieFile  =  "{}-{}-{}.cookie".format(iName, gNowTimeFunc(), uuid.uuid4())
        self.__mCookieFile = "{}{}.cookie".format(gConfigFileWrapper.getStr('curl', 'cookie_folder'), self._mName)
        self._mResponseHeader = BytesIO()
        self._mResponseData = BytesIO()

    def __constructCurl(self):
        self._mCurl = pycurl.Curl()
        self._mCurl.setopt(pycurl.VERBOSE, gConfigFileWrapper.getBoolean('curl', 'verbose'))
        self._mCurl.setopt(pycurl.CONNECTTIMEOUT, gConfigFileWrapper.getInt('curl', 'connect_timeout'))
        self._mCurl.setopt(pycurl.TIMEOUT, gConfigFileWrapper.getInt('curl', 'timeout'))
        self._mCurl.setopt(pycurl.USERAGENT, gConfigFileWrapper.getStr('curl', 'user_agent'))
        self._mCurl.setopt(pycurl.WRITEHEADER, self._mResponseHeader)
        self._mCurl.setopt(pycurl.WRITEDATA, self._mResponseData)
        self._mCurl.setopt(pycurl.COOKIEJAR, self.__mCookieFile)
        self._mCurl.setopt(pycurl.COOKIEFILE, self.__mCookieFile)
        self._mCurl.setopt(pycurl.SSL_VERIFYPEER, 0)
        self._mCurl.setopt(pycurl.SSL_VERIFYHOST, 0)