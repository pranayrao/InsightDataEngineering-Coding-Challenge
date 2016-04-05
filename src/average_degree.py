# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 01:44:14 2016

@author: pranay
"""
# -*- coding: utf-8 -*-

import sys
import json
import networkx as nx
import itertools
import datetime
from decimal import *
import time
import numpy as np

exec_start_time = time.time()

#dictionary with created_at as key and the hashtags list as values
data_dict = dict()

#list for storing and maintaining the graph edges
edgelist = list()

#function to extract hashtag and and created_at from each line of input text file
def extractHashtagCreatedAt(inputText):
    hashtag = list()
    created_at = ""
    jsonData = json.loads(inputText)

    if "entities" in jsonData:
        ent = jsonData["entities"]
        if "hashtags" in ent:
            hashtagList = ent["hashtags"]
            if hashtagList:        
                hashtag = [h['text'] for h in hashtagList]
                hashtag = list(hashtag)

    if "created_at" in jsonData:
        created_at = jsonData["created_at"]
        created_at = datetime.datetime.strptime(created_at,'%a %b %d %H:%M:%S +0000 %Y')
    return hashtag, created_at

#function to calculate the difference between the max created_at and the current
#value of created_at and check if it is more than 60 seconds behind the max value
def checkSlidingWindow(t1,t2):
    difference = (t2-t1).total_seconds()    
    if difference < 60:
         return True
    else:
            return False

#function for generating edges from an list of hashtags passed as an argument
def getEdgeList(hashtag):
            #creating list of tuples of various combination of hashtags present in a 
            #hashtag list                      
            hashlist = list(itertools.combinations(hashtag, 2))
            return hashlist
 
#function to evict edges that are older than 60 seconds from the maximum
#value of created_at processed
def evictEdges():
    global edgelist
    global data_dict
    old_created_at=[]
    #finding the maximum value of created_at
    max_created_at = max(data_dict.keys())
    all_created_at=data_dict.keys()
    for createdat in all_created_at:
        if not checkSlidingWindow(createdat,max_created_at):
                    #find the hashtag values of the created_at that is outside
                    #rolling window
                    invalidHashtags=data_dict[createdat]
                    invalidEdges=getEdgeList(invalidHashtags)
                    #remove those edges from the edge list                    
                    edgelist=list(set(edgelist)-set(invalidEdges))
                    old_created_at.append(createdat)
    #update the dictionary to its latest state  
    data_dict = dict( (key, value) for key,value in data_dict.items() if key not in old_created_at)
    
#function to update the edge list 
def updateEdgeList(hashtag):
    global edgelist
    #function call to get the edge list for the current hashtag values
    edges_to_add=getEdgeList(hashtag)
    #add the new edge list returned above to the existing edge list
    edgelist = list(set(edgelist + edges_to_add))
    #function call for removing edges that fall outside the window    
    evictEdges()
   
#function to calculate the rolling average degree
def calAvgDegree():    
    global edgelist
    global roll_avg
    roll_avg = 0
    #creating a graph    
    g = nx.Graph()
    #creating a numpy array for faster iteration
    numpy_array = np.array(edgelist)
    for arr in numpy_array:    
        #adding edges to the graph        
        g.add_edges_from(list(itertools.combinations(arr,2)))
    #calculating the degree for each node in the graph    
    deg = g.degree()
    if deg.values():
         #calculating the rolling average and converting the float
         roll_avg = float(sum(deg.values()))/len(deg.values())
    #truncating the rolling average to two decimal places
    return str(Decimal(roll_avg).quantize(Decimal('.01'),rounding=ROUND_DOWN))

#function to read the input file and write the results to the output file
#line by line
def tweetParser(tweettxt,outputtxt):
    global data_dict    
    global edgelist
    with open(tweettxt, "r") as infile, open(outputtxt, "w") as outfile:
        for line in infile:
                  #call to function for extracting only the required information 
                  #for each line in the input file
                  hashtag, created_at = extractHashtagCreatedAt(line)
                  if created_at:
                               # creating a dictionary with created_at as key
                               # the hashtags list as values
                               data_dict[created_at]=hashtag
                               #function call for updating the edgelist with
                               #hashtag list and created_at as arguments
                               updateEdgeList(hashtag)
                               #function call for calculating average degree
                               avgDegree=calAvgDegree()
                               #write each result to a new line in output file
                               outfile.write(str(avgDegree)+'\n')

def main():
    #'tweet_input/tweets.txt'    
    tweettxt = sys.argv[1]
    #'tweet_output/output.txt'
    outputtxt = sys.argv[2]
    #call to function for reading data from and writing data to txt files
    tweetParser(tweettxt,outputtxt)
    
if __name__ == '__main__':
    main() 

print "Time taken to complete : %s seconds" % (time.time() - exec_start_time) 
print "The output.txt file is in tweet_output folder"
print ""
