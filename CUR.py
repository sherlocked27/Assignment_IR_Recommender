# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 14:40:05 2018

@author: rishi
"""

import requests, zipfile, os, io, pandas as pd
import numpy as np
from numpy import linalg as LA
import random
from sklearn.metrics import mean_squared_error as mse

#from surprise import Datatset

new_data=pd.DataFrame()
data_csv=pd.read_csv("./dataset/ratings.csv")
del data_csv['timestamp']
new=data_csv.pivot(index='userId', columns='movieId', values='rating')
new=new.fillna(0)
final=np.array(new)

sq_sum=0
for i in range(len(final)):
    for j in range(len(final[0])):
        sq_sum=sq_sum+final[i][j]**2
row_sum=[0 for i in range(len(final))]
col_sum=[0 for i in range(len(final[0]))]

for i in range(len(final)):
    for j in range(len(final[0])):
        row_sum[i]=row_sum[i]+final[i][j]**2
 
for j in range(len(final[0])):
    for i in range(len(final)):
        col_sum[j]=col_sum[j]+final[i][j]**2

for i in range(len(row_sum)):
    row_sum[i]=(row_sum[i]/sq_sum)
    
for i in range(len(col_sum)):
    col_sum[i]=(col_sum[i]/sq_sum)

c=0.4*len(final) 
col_rand=[]
row_rand=[]   
for i in range(int(c)):
    col_rand.append(random.randint(-1,len(final[0])-1))
    row_rand.append(random.randint(-1,len(final)-1))

C=final[:,col_rand]
R=final[row_rand,:]

for i in range(len(C[0])):
    for j in range(len(C)):
        C[j][i]=C[j][i]/((int(c)*col_sum[col_rand[i]])**(0.5))

for i in range(len(R)):
    for j in range(len(R[0])):
        R[i][j]=R[i][j]/((int(c)*row_sum[row_rand[i]])**(0.5))

W=[]
for i in row_rand:
    temp=[]
    for j in col_rand:
        temp.append(final[i][j])
    W.append(temp)
W=np.array(W)


prod=np.dot(W,W.T)
lambd , U =LA.eig(prod)
prod2=np.dot(W.T,W)
lambd_2 , V = LA.eig(prod2)
V_T = V.T
lambd=np.sqrt(lambd)
sigma = np.diag(lambd)

for i in range(len(sigma)):
    for j in range(len(sigma[0])):
        if(sigma[i][j]!=0):
            sigma[i][j]=1/sigma[i][j]
U=np.dot(V,np.dot(sigma,U.T))

new_final1=np.dot(C,np.dot(U,R))

rms2 = np.sqrt(mse(final,new_final1))           #Spearman and RMSE
temp=rms2*(610*9724)
temp=temp**2
num_val=610*9724
spear_error=1 - ((6*temp)/(num_val*(num_val**2-1)))
print("RMS = ",rms2," Spearman Error = ",spear_error) 


a=[]                                  #Top k error
for i in range(610):
    for j in range(9724):
        a.append((new_final1[i][j],i,j))
a.sort(reverse=True)
sum=0
for i in range(50):
    sum=sum+(a[i][0]-final[a[i][1]][a[i][2]])**2
top_k_error=np.sqrt(sum)/50      

print("Top k error = ",top_k_error)
