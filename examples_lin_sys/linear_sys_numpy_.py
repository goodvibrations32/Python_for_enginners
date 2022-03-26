"""
Λύση γραμμικού συστήματος 3x + y = 9 , x + 2y = 8
με χρήση της linalg.solve()
"""
#%%
import numpy as np
from numpy import linalg as LA

A = np.array([[3,1],[1,2]])
B = np.array([[9],[8]])

x = np.linalg.solve(A,B)
print ('solution is x =', x[0], 'y =', x[1])
check_of_opp = np.dot(A, x)
# %%
