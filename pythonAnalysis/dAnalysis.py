# title          : dataSet Analysis
# description    : Python application that provides analysis on Kaggle dataset
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



#Functions from preProcess Class
from preProcess import preProcessing

##############################################
###############READ IN FILES##################
##############################################

yelpRevs = csv.reader(open("yelp_files/yelp_review.csv", encoding = "utf-8"))
yelpBus = csv.reader(open('yelp_files/yelp_business.csv', encoding="utf8"))
myFile = open("output.txt","w") 

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def restOfReviews(userID, someFile, theHash):
	for row in someFile:
		if row[1]==userID:
			print(row)


#def allMessages():
	#print("DONE")
	#return RSA, IS, rvM, USD, OID, match, nextLine, OR, someList
	#print("VALUES RETURNED")


#############################################
#################MAIN METHOD#################
#############################################

testOut = preProcessing(1)
myBHash= testOut.reviewHash(yelpRevs, testOut.filterRest(yelpBus))
for x in range(5):
	myFile.write("Randomly selecting auxiliary information...."+ "\n")
	randomRecords = testOut.genRandRec(myBHash)
	randomVal = randomRecords[0][0]
	userID = randomRecords[1]
	myFile.write("Information Selected, See Below:"+ "\n")
	myFile.write(str(randomVal)+ "\n")

	matches =[]
	for key in myBHash:
		#print(key)
		for item in myBHash[key]:
			if (randomVal[0]==item[0]) and (abs(int(randomVal[1])-int(item[1]))<=2) and (days_between(randomVal[2], item[2])<1):
				matches.append(key)

	myFile.write("THIS IS THE USER ID DETECTED: "+ str(matches[0]) + "\n")
	#print("THIS IS THE USER ID DETECTED", matches[0])
	#print("THIS IS ORIGINAL ID", userID)
	myFile.write("THIS IS THE ORIGINAL ID: "+ str(matches[0])+ "\n")
	#print("THE TWO ARE A MATCH! BECAUSE OF THIS WE CAN ALSO ACCESS THE REST OF THE REVIEWERS REVIEWS")
	myFile.write("THE TWO ARE A MATCH! BECAUSE OF THIS WE CAN ALSO ACCESS THE REST OF THE REVIEWERS REVIEWS"+ "\n")
	myFile.write("\n")
	myFile.write("OTHER REVIEWS:"+ "\n")
	myFile.write("\n")
	someList = []
	for item in myBHash[matches[0]]:
		myFile.write("Business Name: " + str(item[0])+ "\n")
		myFile.write("Stars: " + str(item[1])+ "\n")
		myFile.write("Date of Review: " + str(item[2])+ "\n")
		myFile.write("\n")





