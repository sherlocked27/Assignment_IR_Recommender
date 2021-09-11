# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:53:49 2018

@author: rishi
"""
import pandas as pd
import numpy as np
from numpy import linalg as LA
from sklearn.metrics import mean_squared_error as mse

#from surprise import Datatset

new_data=pd.DataFrame()
data_csv=pd.read_csv("./dataset/ratings.csv")
del data_csv['timestamp']
new=data_csv.pivot(index='userId', columns='movieId', values='rating')
new=new.fillna(0)
final=np.array(new)
                        #after preprocesssing
prod=np.dot(final,final.T)

#A=np.array([[3 , 1 , 1],[-1 , 3 , 1]])
#prod2=np.dot(A,A.T)
#u , v =LA.eig(prod2)

lambd , U =LA.eig(prod)             
prod2=np.dot(final.T,final)
lambd_2 , V = LA.eig(prod2)
V_T = V.T                            
lambd=np.sqrt(lambd)
sigma = np.diag(lambd)
zero_mat = np.zeros((610,9114))
sigma=np.concatenate((sigma,zero_mat),axis=1)  

new_final1 = np.dot(U,np.dot(sigma,V_T))   #After SVD

rms = np.sqrt(mse(final,new_final1))   # Rms and spearman error
temp=rms*(610*9724)
temp=temp**2
num_val=610*9724
spear_error=1 - ((6*temp)/(num_val*(num_val**2-1)))
print("RMS = ",rms," Spearman Error = ",spear_error)

a=[]                                  #Top k error
for i in range(610):
    for j in range(9724):
        a.append((final[i][j],i,j))
a.sort(reverse=True)
sum=0
for i in range(50):
    sum=sum+(a[i][0]-new_final1[a[i][1]][a[i][2]])**2
top_k_error=np.sqrt(sum)/50        
print("Top k error = ",top_k_error)


###################### 90% #######################


print(" For 90% ")
sq=0;
new_sq=0
for j in range(len(lambd)):
    sq=sq+lambd[j]*lambd[j]
for j in range(len(lambd)-1,0,-1):
    new_sq=new_sq+lambd[j]**2
    if(((sq-new_sq)/sq)<0.9):         #To check 90% retained energy
        req=j+1
        break
new_lambd=np.delete(lambd,slice(req,610),axis=0)
sigma = np.diag(new_lambd)
zero_mat = np.zeros((len(new_lambd),9724-len(new_lambd)-(610-req)))
sigma=np.concatenate((sigma,zero_mat),axis=1)
new_U=np.delete(U,slice(req,610),axis=1)
new_V_T=np.delete(V_T,slice(9724-(610-req),9724),axis=0)


new_final2 = np.dot(new_U,np.dot(sigma,new_V_T))

rms2 = np.sqrt(mse(final,new_final2)) #RMS error and Spearman error
temp=rms2*(610*9724)
temp=temp**2
spear_error_2=1 - ((6*temp)/(num_val*(num_val**2-1)))
print("RMS = ",rms2," Spearman Error = ",spear_error_2)

a2=[]                                   #Top k error
for i in range(610):
    for j in range(9724):
        a2.append((new_final2[i][j],i,j))
a2.sort(reverse=True)
sum=0
for i in range(50):
    sum=sum+(a2[i][0]-final[a[i][1]][a[i][2]])**2
top_k_error2=np.sqrt(sum)/50 
print("Top k error = ",top_k_error2)
