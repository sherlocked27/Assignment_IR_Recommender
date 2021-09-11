# Recommendor System


Below is the list of the algorithms used to implement recommendor systems which have been implemented which include Collaborative filtering, Singular Value Decomposition and CUR.


## Functionality Implemented


 1. Collaborative Filtering (calculating similarity by users and predicting missing ratings)
  
2. Collaborative Filtering using global baseline approach.
  
3. SVD

4. SVD with 90% retained energy

5. CUR with sampling of rows and columns with replacement
  
6. CUR with sampling of rows and columns without replacement



# The Dataset 
 * [Movie Rating Corpus](http://www.ieor.berkeley.edu/~goldberg/jester-data/) - dataset contains users and their ratings.



## Software/frameworks used:

 * [python-Numpy, Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html) 

    
1. Install pip: sudo apt-get install python-pip
   
2. Install Numpy : sudo pip install -U numpy
   
3. Install pandas : sudo pip install pandas
   
    

*Check for istallation by Opening up a Python prompt by running the following:


		python


​		
At the prompt, type the following:
​		
​		
>>> import pandas

>>> import numpy

>>> print numpy.__version__


 * [python-xlrd module](https://www.loomio.org/) - 


1. Install xlrd: pip install xlrd

2. Install xlwt: pip install xlwt

 


## Platforms:

 * To run recommender system make sure you got python installed.


## Run:
 * nevigate to IR_AS3 directory.
 * change path to the dataset in files to run 
 * use python3 filename. 



## **RESULT**



| TECHNIQUE                    | RMSE   | PRECISION    AT  TOP 50 | SPEARMAN  CORREALTION | TIME  TAKEN (in sec) |
| ---------------------------- | ------ | ----------------------- | --------------------- | -------------------- |
| Collaborative                | 0.08   | 1.389                   | 0.999                 | 300                  |
| Collaborative  with baseline | 0.1581 | 1.440                   | 0.999                 | 180                  |
| SVD                          | 0.60   | 1.53                    | 0.9999                | 600                  |
| SVD  with 90%                | 0.58   | 1.55                    | 0.999                 | 450                  |
| CUR (with  repetition)       | 495.81 | 14.82                   | 0.998                 | 300                  |
| CUR  (without repetition)    | 2260   | 568                     | 0978                  | 200                  |