# title          : preProcess.py
# description    : Python application that instantiates dataStructues for class
# author         : Daniel Brett, 
# date           : Monday, May 7th 2018
# python_version : 3.5
# ==================================================



#####################################
##########Relevant Libraries#########
#####################################


import os, csv
#from http.server import BaseHTTPRequestHandler, HTTPServer
import itertools
import math, random
from datetime import datetime
import statistics, operator
import heapq
import numpy as np
import collections
import matplotlib.pyplot as plt

#PORT_NUMBER = int(os.environ.get('PORT', 8084))

##############################################
###############READ IN FILES##################
##############################################

yelpRevs = csv.reader(open("yelp_files/yelp_review.csv", encoding = "utf-8"))
yelpBus = csv.reader(open('yelp_files/yelp_business.csv', encoding="utf8"))

#class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

class preProcessing(object):

	def __init__(self, num):
		self.num=num

	#hasMap that filters ID to rest name
	def filterRest(self, busFile):
		restHash = {}
		for row in busFile:
			if "Restaurant" in row[12]:
				restHash[row[0]]=row[1]
		return restHash

	#Narrow down reviews. Only want ones about 
	#restaurants. Get rid of extraneous info
	def reviewHash(self, revFile, busHash):
		print("Building HashMap Data Structure....")
		userHash = {}
		for row in revFile:
		#could search through the myHash here, but that could will
		#be slow. O(n^2). 
			if row[2] in busHash.keys():
				if row[1] not in userHash:
					userHash[row[1]] = [(busHash[row[2]], row[3], row[4])]
				else:
					userHash[row[1]].append((busHash[row[2]], row[3], row[4]))
		print("HashMap Constructed")
		return userHash

	def genRandRec(self, someHash):
		numTRecs = 3
		reviewSet = []
		flag = True 
		while flag:
			randRec = random.choice(list(someHash.keys()))
			if len(someHash[randRec])>=numTRecs: #and len(someHash[randFRec])>=numFRecs:
				flag = False
		for i in range(numTRecs):
			reviewSet.append(someHash[randRec][i])
		return reviewSet, randRec

	def sim(self, aux, rec):
		if (aux[0]==rec[0]) and (abs(int(aux[1])-int(rec[1]))<=2) and (self.days_between(aux[2], rec[2])<=7):
			return True
		return False


	def getWT(self, someRec, uHash):
		suppI=0
		for key in uHash:
			for val in uHash[key]:
				if someRec[0] in val:
					suppI+=1
		if suppI==0:
			return 0
		else:
			return 1.0/(float(math.log(suppI)))

	def makeWTHash(self, auxList, someHash):
		wtHash={}
		for record in auxList:
			wtHash[record]=getWT(record, someHash)
		return wtHash
















#randomReviews = testOut.genRandRec(myBHash)
#print("Days Between", randomReviews[0], " And ", randomReviews[1],  str(testOut.days_between(randomReviews[0], randomReviews[1])))









	