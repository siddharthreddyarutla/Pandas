# -*- coding: utf-8 -*-
"""pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SQKAbcNO9r3drzly803kGTjE_PJufok1

# Pandas
"""

import pandas as pd

"""Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the python programming language."""

import numpy as np
import pandas as pd
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)

s = pd.Series([1,2,3,4,5])

#retrieve the first element
print(s[0])

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print(s[0])

print(s[:3])

print(s['a'])

#retrieve multiple elements
print(s[['a','c','d']])

"""Dataframe"""

import pandas as pd
arr={'sid':0, 'siddu':1, 'siddharth':2}
res=pd.Series(arr)
print(res)

import pandas as pd
s=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])

s

print(s[0])

print(s[:2])

print(s[2:])

print(s['a'])

print(s["c"])

print(s["e"])

#retrieve multiple elements
print(s[['a','c','d']])

import pandas as pd
import numpy as np
arr=np.array([1,2,3,4,5])
s=pd.Series(arr)
s

import pandas as pd
import numpy as np
arr=np.array(['cat','dog','rat','cow','pig'])
s=pd.Series(arr,index=[100,101,102,103,104])
s