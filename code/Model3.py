#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sko.GA import GA
B=0
B2=0
b1=0
b2=0
p=0
n=0
n1=1
m1=1
b=3
k=3
v=5
v1=5


# In[2]:


import math
def demo_func2(x):
    n, k, x3 = x
    n=int(n)
    k=int(k)
    nn=0
    d=10
    v=v1*math.log(1/3/(k/(10+4*k)))
    return (p+B*n1*2)*(d+4*k)*(n-1)/v/k+b*((2*B*n1+p)/4/n)*(B*2*n1+p)

    
def demo_func1(y):
    n, m, g = y
    d=10
    dd=4
    x=g*p
    tt=30
    b=20
    return ((d+k*dd)*(n-1)*x)/2 +((d+k*dd)*(m-1)*(p-x))/2   +tt*(p-x)+((d+k*dd)*(n-1)*x)/(v*k)+((d+k*dd)*(m-1)*(p-x))/(v*k)     +b/2*(x/n)*x/(n*k)   +b/2*((p-x)/m)*(p-x)/(m*k)


# In[3]:


list=[]
for i in range(12):
    list.append(4)
for i in range(23):
    list.append(5)
for i in range(9):
    list.append(6)
for i in range(22):
    list.append(7)
for i in range(36):
    list.append(8)
for i in range(39):
    list.append(9)
for i in range(48):
    list.append(10)
for i in range(47):
    list.append(11)  
dict={}
dict[4]=77
dict[5]=107
dict[6]=109
dict[7]=99
dict[8]=80
dict[9]=300
dict[10]=224
dict[11]=229
interval={}
interval[4]=600
interval[5]=313
interval[6]=800
interval[7]=327
interval[8]=200
interval[9]=184
interval[10]=150
interval[11]=153


# In[4]:


x=[]
y=[]
time=0
for i in range(50):
    time+=576
    x.append(time/3600)
    y.append(0)
for i in range(102):
    current=list[i]
    p=dict[current]/1
    t=interval[current]
    time+=t
    x.append(time/3600)
    ga = GA(func=demo_func1, lb=[n1,m1,0.1], ub=[30,30,1], max_iter=200,n_dim=3)
#    ga = GA(func=demo_func2, lb=[n1,2,2], ub=[50,20,3], max_iter=300,n_dim=3)

    best_x, best_y = ga.fit()
    n,l,m=best_x
    y.append(n+l)
    n1=int(n)
    m1=int(m)
    E=(2*n)/(b+(n-1)*(10+4*k)/v)*k
    B=B+p/2/n-t*E/2/n
    
    B=int(B)
    if(B<0):
        B=0
        
    print(i+1,p,t,int(n),int(l),m,k,int(B),E)
    
    
    
for i in range(102,236):
    current=list[i]
    p=dict[current]/1
    t=interval[current]
    time+=t
    x.append(time/3600)
#     ga = GA(func=demo_func1, lb=[1,1,0.1], ub=[30,30,1], max_iter=200,n_dim=3)
    ga = GA(func=demo_func2, lb=[n1,2,2], ub=[50,20,3], max_iter=300,n_dim=3)

    best_x, best_y = ga.fit()
    n,l,m=best_x
    y.append(2*n)
    n1=int(n)
    E=(2*n)/(b+(n-1)*(10+4*k)/v)*k
    B=B+p/2/n-t*E/2/n
    
    
    B=int(B)
    if(B<0):
        B=0

#     print(i+1,p,t,int(n),int(l),m,k,int(B),E)
    print(i+1,p*2,t,int(n),int(l),int(B),E)
    


# In[8]:


# import pandas as pd
# import matplotlib.pyplot as plt
# FitV_history = pd.DataFrame(ga.FitV_history)
# fig, ax = plt.subplots(2, 1)
# ax[0].plot(FitV_history.index, FitV_history.values, '.', color='red')
# plt_max = FitV_history.max(axis=1)
# ax[1].plot(plt_max.index, plt_max, label='max')
# ax[1].plot(plt_max.index, plt_max.cummax())
# plt.show()


import matplotlib.pyplot as plt
import numpy as np
# y=[]
# for i in range(16):
#     y.append(0)
# for i in range(20):
#     y.append(5)
# y.append(12)
# y.append(17)
# y.append(23)
# y.append(25)
# y.append(26)
# y.append(26)
# y.append(26)
# y.append(26)
# y.append(26)
# y.append(26)
# y.append(27)
# y.append(28)
# x = np.linspace(0,23,48)

plt.scatter(x,y)
plt.figure(figsize=(36,36.5))
plt.show()


# In[6]:


best_x


# In[7]:


best_y


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




