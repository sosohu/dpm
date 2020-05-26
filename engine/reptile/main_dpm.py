#!/usr/bin/env python
# encoding:utf-8

import sys
import time

sys.path.insert(0, "C:\\work\\dpm")

from engine.common.start_up import gConfigFileWrapper
from engine.reptile.download_dpm import CDownloadDpm
from engine.reptile.metadata_dpm import gMetadataDpm
from engine.reptile.download_dpm import downloadDpmRun
from engine.common.thread_pool import CThreadPool

def downloads(iOffset, iNum):
    lThreadPool = CThreadPool(iNum)
    lThreadPool.setRunner(downloadDpmRun)
    for j in range(iNum):
        lThreadPool.addArgs((gConfigFileWrapper.getInt('dpm', 'resoure_category'), iOffset + j, gConfigFileWrapper.getStr('dpm', 'save_path')))
        
    start_time = time.time()
    lThreadPool.run()
    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))
    gMetadataDpm.dumpResourceMetadata()

def main():
    start_time = time.time()
    lStartPage = gConfigFileWrapper.getInt('dpm', 'start_page')
    lEndPage = gConfigFileWrapper.getInt('dpm', 'end_page')
    lTotalPage = lEndPage - lStartPage  # [lStartPage, lEndPage)
    lThreadsNum = gConfigFileWrapper.getInt('dpm', 'thread_num')

    lLeft = lTotalPage % lThreadsNum
    for i in range(0, lTotalPage - lLeft, lThreadsNum):
        downloads(i + lStartPage, lThreadsNum)

    if lLeft != 0:
        downloads(lTotalPage - lLeft, lLeft)

    end_time = time.time()
    print("--- total %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()