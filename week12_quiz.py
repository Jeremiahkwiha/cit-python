import pandas as pd
import numpy as np
import statistics as st

#Number 1
"""
Ans = [1, 2, 3] + [4, 5, 6] = [5, 7, 9]
"""

#QN 2

arr = np.array([0,0,0,0,0,0,0,0,0,0])
print(arr.reshape(2,5))


#QN 3

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
mode = st.mode(data)
#print(mode)

median = np.median(data)
#print(median)

SD = st.stdev(data)
#print(SD)
print(f"mode is : {mode}, median is : {median} and standard deviation is : {SD}")


#QN 4
for i in range(36):
    array = np.arange(36).reshape(6,6)
print(array)


#QN 5
for i in range(12):
    array2 = np.arange(12).reshape(3,4)
    array2 = array2.reshape(2,6)
print(array2)


#QN 6
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
data = data.reshape(1,9)
print(data)














































#  https://forms.gle/7L1AhkEU6Uf2aNhc6
