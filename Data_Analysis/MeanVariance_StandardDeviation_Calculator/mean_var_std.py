import numpy as np
import pandas as pd

def calculate(list):
 try:
    if len(list) ==9: 
     num_arry= np.array(list)#change python list into a numpy array
     #shaping into a 3x3 matrix
     newarry= num_arry.reshape(3,3)
     #creating a dictionary
     calculations= pd.DataFrame({
       'mean':[
          #one way to calculate each row(axis=0)/col(axis=1) then returning a list
          newarry.mean(axis=0),
          newarry.mean(axis=1),
          newarry.mean() ],
         #one way to calculate each row(axis=0)/col(axis=1) then returning a list
       'variance':[
          np.var(newarry,axis=0),
          np.var(newarry,axis=1),
          newarry.var()
       ],
       'standard variation':[
          np.std(newarry,axis=0),
          np.std(newarry,axis=1),
          newarry.std() ],
       'max':[np.max(newarry,axis=0),
             np.max(newarry,axis=1),
             newarry.max()
            ],
       'min':[np.min(newarry,axis=0),
             np.min(newarry,axis=1),
             newarry.min()
            ],
       'sum':[np.sum(newarry,axis=0),
             np.sum(newarry,axis=1),
             newarry.sum()
            ]
         }) 
 except ValueError:
    print("list must contain nine member")
    
 return calculations