# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 01:46:41 2018

@author: rishi
"""

import pandas as pd
import numpy as np


#from surprise import Datatset

new_data=pd.DataFrame()
data_csv=pd.read_csv(".dataset/ratings.csv")
del data_csv['timestamp']
new=data_csv.pivot(index='userId', columns='movieId', values='rating')
new=new.fillna(99)
final=np.array(new)
new_final=np.delete(final,slice(101,610),axis=0)
new_final=np.delete(new_final,slice(5000,9724),axis=1)

new_data2=pd.DataFrame(new_final)
new_data2.to_csv('5000dataset.csv', index= False , header=False)

