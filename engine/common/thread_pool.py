#!/usr/bin/env python
# encoding:utf-8

import threading
import threadpool

from engine.common.start_up import gLogger

class CThreadPool():
	def __init__(self, num):
		self.__mNum = num
		self.__mPool = threadpool.ThreadPool(num)
		self.__mFuncVar = []
		self.__mRunner = None

	def setRunner(self, iRunner):
		if not callable(iRunner):
			gLogger.error("Expect a function but input type is: {}".format(type(iRunner)))
			return

		self.__mRunner = iRunner
		
	def addArgs(self, iArgs):
		if not type(iArgs) is tuple:
			gLogger.error("Expect a tuple but input type is: {}".format(type(iArgs)))
			return
		
		self.__mFuncVar.append((iArgs, None))
		
	def run(self):
		if self.__mNum != len(self.__mFuncVar):
			gLogger.error("The number of FuncVar is not match. Expect {} but now is {}.".format(self.__mNum, len(self.__mFuncVar)))
			return

		gLogger.debug("Start to run {} in multi threads. Nums: {}. FuncVars: {}.".format(self.__mRunner, self.__mNum, self.__mFuncVar))

		lRequests = threadpool.makeRequests(self.__mRunner, self.__mFuncVar)
		[self.__mPool.putRequest(req) for req in lRequests]
		self.__mPool.wait()