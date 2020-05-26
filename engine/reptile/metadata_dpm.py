#!/usr/bin/env python
# encoding:utf-8

import json
import os

from engine.common.start_up import gConfigFileWrapper
from engine.common.start_up import gLogger

class CMetadataDpm():
    def __init__(self):
        self.__mResourceMetadata = {} # uuid <-> {}
        self.loadResourceMetadata()
        return

    def __del__(self):
        return

    def loadResourceMetadata(self):
        if os.path.exists(gConfigFileWrapper.getStr('dpm', 'metadata_file')):
            with open(gConfigFileWrapper.getStr('dpm', 'metadata_file'), 'r') as in_file:
                lLines = in_file.readlines()
                for lLine in lLines:
                    lJLine = json.loads(lLine)
                    if lJLine['uuid']:
                        self.__mResourceMetadata[lJLine['uuid']] = lJLine
                    else:
                        gLogger.error("Resource {} does not have uuid".format(lJLine))
                        return

    def dumpResourceMetadata(self):
        with open(gConfigFileWrapper.getStr('dpm', 'metadata_file'), 'w') as out_file:
            for _, v in self.__mResourceMetadata.items():
                out_file.write(json.dumps(v, ensure_ascii=False).encode('utf8').decode())
                out_file.write("\n")

    def isExistedResource(self, iUuid):
        return iUuid in self.__mResourceMetadata

    def insertResource(self, iUuid, iData):
        if self.isExistedResource(iUuid):
            gLogger.error("The resource {} has existed".format(iUuid))
            return

        self.__mResourceMetadata[iUuid] = iData

gMetadataDpm = CMetadataDpm()