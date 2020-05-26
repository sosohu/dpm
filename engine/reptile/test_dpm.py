#!/usr/bin/env python
# encoding:utf-8

import sys
import time

sys.path.insert(0, "C:\\work\\dpm")

from engine.common.start_up import gConfigFileWrapper

from engine.reptile.metadata_dpm import gMetadataDpm

gMetadataDpm.dumpResourceMetadata()