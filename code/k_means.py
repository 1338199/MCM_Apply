import numpy as np
import random
import re
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D 
def show_fig():
    dataSet = loadDataSet()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataSet[:, 0], dataSet[:, 1])
    plt.show()

def calcuDistance(vec1, vec2):
    if vec1[0] == vec2[0]:
        d = 0
    else:
        d = 1
    dis = np.sqrt(np.sum(np.square(vec1[1:] - vec2[1:]))) + 0.15*d
    return dis  

def loadDataSet():
    dataSet = pd.read_csv("final_data_set.csv").values
    dataSet = random.sample(list(dataSet), 1000)
    return dataSet

def initCentroids(dataSet, k):
    dataSet = list(dataSet)
    return random.sample(dataSet, k)

def minDistance(dataSet, centroidList):
    clusterDict = dict()
    k = len(centroidList)
    for item in dataSet:
        vec1 = item
        flag = -1
        minDis = float("inf") 
        for i in range(k):
            vec2 = centroidList[i]
            distance = calcuDistance(vec1, vec2) 
            if distance < minDis:
                minDis = distance
                flag = i  
        if flag not in clusterDict.keys():
            clusterDict.setdefault(flag, [])
        clusterDict[flag].append(item)  
    return clusterDict  

def getCentroids(clusterDict):
    centroidList = []
    for key in clusterDict.keys():
        centroid = np.mean(clusterDict[key], axis=0)
        centroidList.append(centroid)
    return centroidList 


def getVar(centroidList, clusterDict):
    sum = 0.0
    for key in clusterDict.keys():
        vec1 = centroidList[key]
        distance = 0.0
        for item in clusterDict[key]:
            vec2 = item
            distance += calcuDistance(vec1, vec2)
        sum += distance
    return sum

def showCluster(centroidList, clusterDict,ang1,ang2):
    colorMark = ['r', 'b', 'g', 'k', 'y', 'w','m'] 
    fig = plt.figure() 
    ax = Axes3D(fig) 
    
    for key in clusterDict.keys(): 
        ax.scatter(centroidList[key][0], centroidList[key][1], centroidList[key][2],marker = '^', s=30, c=colorMark[key])
        for item in clusterDict[key]:
            ax.scatter(item[0], item[1],item[2], c=colorMark[key],s=6)
    ax.view_init(ang1,ang2)

def test_k_means(k):
    dataSet = loadDataSet()
    centroidList = initCentroids(dataSet, k)
    clusterDict = minDistance(dataSet, centroidList)
    newVar = getVar(centroidList, clusterDict)
    oldVar = 1 
    times = 2
    while abs(newVar - oldVar) >= 0.00001:
        centroidList = getCentroids(clusterDict)
        clusterDict = minDistance(dataSet, centroidList)
        oldVar = newVar
        newVar = getVar(centroidList, clusterDict)
        times += 1
        #showCluster(centroidList, clusterDict)
    return centroidList,clusterDict