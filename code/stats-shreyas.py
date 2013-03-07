#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from http://www.fec.gov/disclosurep/PDownload.do"""

import fileinput
import csv

total = 0
valueList = []

for row in csv.reader(fileinput.input()):
    
    #print(type(valueList))

    if not fileinput.isfirstline():
        total += float(row[9])
        # type (float(row[9]))
        ###
        # TODO: calculate other statistics here
        # You may need to store numbers in an array to access them together
        ##/
        valueList.append(float(row[9]))



# list operations in general
valueList.sort()
listLength = len(valueList)


def calcMedian(numList):

    if listLength%2 == 0:
        # even no of observations in the list
        mid = listLength/2
        #print numList[mid], numList[mid+1]

        median = (numList[mid] + numList[mid +1])/2

    else:
        mid = (listLength+1)/2

        median = numList[mid]
        # print numList[mid]

    return median


def calcMean(numList):
    mean = total/listLength

    return mean



medianStat = calcMedian(valueList)
meanStat = calcMean(valueList)

def calcStandardDeviation(numList):
    deviationSq = 0
    deviationSqSum = 0


    for i in numList:
        deviationSq = (i - meanStat)**2
        deviationSqSum = deviationSqSum + deviationSq


    variance = deviationSqSum/listLength
    stdDev = variance**0.5

    return stdDev


stdDevStat = calcStandardDeviation(valueList)

###
# TODO: aggregate any stored numbers here
#
##/

##### Print out the stats
print "Total: %s" % total
print "Minimum: %s" % valueList[0]
print "Maximum: %s" % valueList[-1]
print "Mean: %s" % meanStat
print "Median: %s" % medianStat
# square root can be calculated with N**0.5
print "Standard Deviation: %s" % stdDevStat

##### Comma separated list of unique candidate names
print "Candidates: "

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    ###
    # TODO: replace line below with the actual calculations
    norm = value
    ###/
    
    return norm

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])

