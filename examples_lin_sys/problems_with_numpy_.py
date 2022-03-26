"""
Προβλήματα και λύσεις με την χρήση της numpy βιβλιοθήκης
"""

#%%
#Επίλυση γραμμικού συστήματος
import numpy as np

def lin_alg_solver_ (A, b):
    B = np.linalg.inv(A)
    x = np.dot(B, b)
    return x

A = np.array([[3,1], [1,2]])
b = np.array([[9], [8]])

print(lin_alg_solver_(A, b))

print(np.linalg.solve(A,b))


# %%
A = ([[0.001,1],[1,1]])
b = ([[1],[2]])


print(lin_alg_solver_(A, b) )
print (np.linalg.solve(A, b))
# %%
