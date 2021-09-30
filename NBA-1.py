t#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:48:39 2019

@author: ajaykrishnavajjala
"""
#%%
import random
from sklearn.tree import DecisionTreeClassifier
#from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
#%%
random.seed(0.13975)
#%%
file = open("/Users/arunkrishnavajjala/Documents/GMU/CS 484/PROJECT/project/boxScore.csv")
#%%
statDict = {"Home": 1.0, "Away": 0.0, "East": 1.0, "West": 0.0, "Win": 1.0, "Loss": 0.0}
#%%
trainDataSet = []
firstKeys = []
secondKeys = []
firstWins = []
secondWins = []
regularKeys = []
#%%
count = 0
for line in file:
    if count >= 1:
        trainData = []
        arr = line.split(",")
        # First Team Data
        trainData.append(statDict[arr[6]])
        trainData.append(statDict[arr[8]])
        trainData.append(float(arr[13])/4.0)
        trainData.append(float(arr[14])/4.0)
        trainData.append(float(arr[15])/4.0)
        trainData.append(float(arr[16])/4.0)
        trainData.append(float(arr[17])/4.0)
        trainData.append(float(arr[18])/4.0)
        trainData.append(float(arr[19])/4.0)
        trainData.append(float(arr[21])/4.0)
        trainData.append(float(arr[22])/4.0)
        trainData.append(float(arr[24])/4.0)
        trainData.append(float(arr[25])/4.0)
        trainData.append(float(arr[27])/4.0)
        trainData.append(float(arr[28])/4.0)
        trainData.append(float(arr[30])/4.0)
        trainData.append(float(arr[31])/4.0)
        trainData.append(float(arr[33]))
        firstKeys.append(float(arr[12]))
        firstWins.append(statDict[arr[9]])
        # Second Team Data
        trainData.append(statDict[arr[62]])
        trainData.append(statDict[arr[64]])
        trainData.append(float(arr[69])/4.0)
        trainData.append(float(arr[70])/4.0)
        trainData.append(float(arr[71])/4.0)
        trainData.append(float(arr[72])/4.0)
        trainData.append(float(arr[73])/4.0)
        trainData.append(float(arr[74])/4.0)
        trainData.append(float(arr[75])/4.0)
        trainData.append(float(arr[77])/4.0)
        trainData.append(float(arr[78])/4.0)
        trainData.append(float(arr[80])/4.0)
        trainData.append(float(arr[81])/4.0)
        trainData.append(float(arr[83])/4.0)
        trainData.append(float(arr[84])/4.0)
        trainData.append(float(arr[86])/4.0)
        trainData.append(float(arr[87])/4.0)
        trainData.append(float(arr[89]))
        # Append to big Data Set
        secondKeys.append(float(arr[68]))
        secondWins.append(statDict[arr[65]])
        trainDataSet.append(trainData)
    if count == 0:
        count += 1
#%%
print("Length of Data Set: " + str(len(trainDataSet)))
print("Length of vals in DataSet: " + str(len(trainDataSet[100])))
print(len(firstWins))
print(len(secondWins))
print(len(secondKeys))
#%%

#%%
print(len(testData))
print(len(firstKeys))
print(len(secondKeys))
print(len(trainDataSet))
#%%
clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
X = trainDataSet
Y = firstKeys
clf = clf.fit(X, Y)
#%%
cmf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
X = trainDataSet
Y = secondKeys
cmf = cmf.fit(X, Y)
#%%
predictionsOne = clf.predict([[1.0, 0.0, 17.0/4.0, 26.0/4.0, 14.0/4.0, 4.0/4.0, 31.0/4.0, 81.0/4.0, 38.0/4.0, 56.0/4.0, 21.0/4.0, 25.0/4.0, 17.0/4.0, 28.0/4.0, 16.0/4.0, 9.0/4.0, 30.0/4.0, 23.0/4.0, 1.0, 1.0, 21.0/4.0, 26.0/4.0, 11.0/4.0, 2.0/4.0, 26.0/4.0, 78.0/4.0, 37.0/4.0, 41.0/4.0, 21.0/4.0, 37.0/4.0, 16.0/4.0, 34.0/4.0, 23.0/4.0, 11.0/4.0, 35.0/4.0, 32.0/4.0]])
predictionsTwo = cmf.predict([[1.0, 0.0, 17.0/4.0, 26.0/4.0, 14.0/4.0, 4.0/4.0, 31.0/4.0, 81.0/4.0, 38.0/4.0, 56.0/4.0, 21.0/4.0, 25.0/4.0, 17.0/4.0, 28.0/4.0, 16.0/4.0, 9.0/4.0, 30.0/4.0, 23.0/4.0, 1.0, 1.0, 21.0/4.0, 26.0/4.0, 11.0/4.0, 2.0/4.0, 26.0/4.0, 78.0/4.0, 37.0/4.0, 41.0/4.0, 21.0/4.0, 37.0/4.0, 16.0/4.0, 34.0/4.0, 23.0/4.0, 11.0/4.0, 35.0/4.0, 32.0/4.0]])
#%%
print(str(predictionsOne) + str(predictionsTwo))
#%%
predictionOne = clf.predict(testData)
predictionTwo = cmf.predict(testData)
#%%
for a,b,c,d in zip(firstKeys, secondKeys, predictionOne, predictionTwo):
    print("Stats")
    print(str(a) + " " + str(b))
    print(str(c) + " " + str(d))




        
        
        
        
        
        
        
        
        
        
        