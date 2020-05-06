import logging
from engine.common.configure_wrapper import CConfigWrapper

gConfigFileWrapper = CConfigWrapper('conf/config.ini')

gLogger = logging.getLogger()
gLogFile = logging.FileHandler(gConfigFileWrapper.getStr('log', 'file'),encoding='utf-8')
gLogFormatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
gLogFile.setFormatter(gLogFormatter) 
gLogger.addHandler(gLogFile)
gLogger.setLevel(gConfigFileWrapper.getInt('log', 'level'))