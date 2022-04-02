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

def main():

    A = np.array([[3,1], [1,2]])
    b = np.array([[9], [8]])

    x = np.linalg.solve(A, b)
    y = lin_alg_solver_(A, b)
    
    print(f"constructed linalg function: \n {y}")
    print (f"numpy linalg function: \n {x}")


    A = ([[0.001,1],[1,1]])
    b = ([[1],[2]])

    x = np.linalg.solve(A, b)
    y = lin_alg_solver_(A, b)
    
    print(f"constructed linalg function: \n {y}")
    print (f"numpy linalg function: \n {x}")

if __name__ == "__main__":
    main()
# %%
