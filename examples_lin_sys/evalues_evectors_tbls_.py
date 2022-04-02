"""
Εστω πίνακας Α Α.shape()= (2,2) 
      | 1   0|
   A =|      |
      | 0   4|

Ιδιοτιμές : λ = 1, 4

Ιδιοδιανύσματα : 

      | 1 |  | 0 |
   x =|   |, |   |
      | 0 |  | 1 |


"""
#%%
import numpy as np

A = np.array([[1,0],[0,4]])
evalues, evectors = np.linalg.eig(A)

#Print the eigenvalues in an array
print('λ= ',evalues)

#Print the eigenvectors in an array
print('x= ',evectors)

#Print the eigenvectors for λ = evalues[i]

for i,j in zip(evalues, evectors) :
    print ('The eigenvector of Table A for λ=',i, 'is x=',j)



# %%
