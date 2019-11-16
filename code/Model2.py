import pandas as pd
import numpy as np
import os
from k_means import calcuDistance,test_k_means,showCluster
L1 = 46.4
L2 = pd.read_csv('dis_city.csv')
V1 = 64.7
V2 = pd.read_csv('velocity.csv')
o = 8.8/100.0
k = 7.13
tCity = pd.read_csv('./city_avg_waiting_time_new.csv')

def cal_extra_Income(te,tw,avgD,v):
    return (te/(tw+avgD/v))*cal_I(avgD,L1,'urban') - (te/(tw+avgD/v))*avgD*o*k

def cal_I(L2,L1,t_type):
    a = 3
    b = 15
    f1 = 14
    f2 = 2.5
    f3 = 3.6
    if t_type == 'airport':
        return  f1 + f2*(b-a) + f3*(L1-b)
    if L2 <= a:
        return f1
    elif a<L2 and L2 <=b:
        return f1+(L2-a)*f2
    else:
        return f1 + f2*(b-a) + f3*(L2-b)
    
def cal_O2(L1):
    return  L1*o*k 

def cal_time_c_a(L1,L2,V2,tw):
    a = 1 
    b = 1 
    y = 1 
    return a*b*(L1/V1 + L2/V2) + y*tw

def cal_W2(tw,V2,avgD,t1):
    L2 = avgD
    L1 = 46.4*V2/50
    I2 = cal_I(L2,L1,'urban')
    Ie = cal_extra_Income(t1-L1/V1,tw,avgD,V2)
    O = cal_O2(L1)
    time = t1#cal_time_c_a(L1,L2,V2,tw)
    print("I2 %f O %f Ie %f time %f"%(I2,O,Ie,time))
    return (I2 - O + Ie)/time

def cal_W1(T,Na,Nc,centroidList):
    a = 1 
    b = 1 
    I1 = cal_I(L2,L1,'airport')
    O1 = L1*o*k
    ts = a*b*L1/V1
    tq = estimate_waiting_time(T,Na,Nc,centroidList)
    print("I1 %f O1 %f ts %f tq %f"%(I1,O1,ts,tq))
    return (I1 - O1)/(ts + tq),ts + tq
def stander(Na,Nc,data_set):
    x = data_set['flight_density']
    Na = (Na-np.min(x))/(np.max(x)-np.min(x))
    x = data_set['taxi_density']
    Nc = (Nc-np.min(x))/(np.max(x)-np.min(x))
    return Na,Nc
def get_origin_waiting_time(t,data_set):
    x = data_set['wait_time']
    t = t*(np.max(x)-np.min(x))+np.min(x)
    print("estimate T %f"%(t))
    return t*13.0/60.0/60.0
def estimate_waiting_time(T,Na,Nc,centroidList):
    data_set = pd.read_csv('data_set_simplify.csv')
    Na,Nc =  stander(Na,Nc,data_set)
    vec1 = np.array([T,Na,Nc])
    judgeList = []
    for i in range(0,len(centroidList)):
        dis = calcuDistance(vec1, centroidList[i][0:-1])
        judgeList.append(dis)    
    min_index = judgeList.index(min(judgeList))
    return get_origin_waiting_time(centroidList[min_index][-1],data_set)

def get_decision(centroidList):
    #data_set =  pd.read_csv('data_set_simplify.csv')
    #data = data_set.sample(n=50)
    data = pd.read_csv('input.csv')
    count = 0
    w1List = []
    w2List = []
    for i in range(0,50):
        temp = data.iloc[i]
        print("time %s T %d Na %f Nc %f"%(temp['time'],int(temp['t_label']/2),temp['flight_density'],temp['taxi_density']),end=" ")
        w1,t1 = cal_W1(int(temp['t_label']/2),temp['flight_density'],temp['taxi_density'],centroidList)
        
        v = V2.iloc[int(temp['t_label'])]['velocity']
        tw = tCity.iloc[int(temp['t_label'])]['avg_time(min/h)']/60.0
        avgD = L2.iloc[int(temp['t_label'])]['avg_dis']
        print("tw: %f v:%f avgD %f"%(tw,v,avgD),end = " ")
        w2 = cal_W2(tw,v,avgD,t1)
        print("w1 %f w2 %f"%(w1,w2))
        print("")
        if w1 < w2:
            count+=1
        w1List.append(w1)
        w2List.append(w2)
    data.insert(6,'w1',w1List)
    data.insert(7,'w2',w2List)
    return count,data
def get_best_desision():
    total = []
    cen = {}
    clu = {}
    for k in range(4,8):
        centroidList,clusterDic = test_k_means(k)
        total.append(get_decision(centroidList))
        cen[k] = centroidList
        clu[k] = clusterDic
    return total,cen,clu
if __name__=='__main__':
    total,cen,clu= get_best_desision()
    print(total)