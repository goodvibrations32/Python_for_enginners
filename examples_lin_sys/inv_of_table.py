"""
Συνάρτηση linalg.inv()
"""
#%%
import numpy as np

A = np.array([[3,1],[1,2]])
B = np.linalg.inv(A)
print("Inverse of A =", B)
print('Check of solution',np.dot(A,B))
# %%
