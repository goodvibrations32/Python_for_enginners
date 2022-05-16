#%%
# Ασκηση 1
import matplotlib.pyplot as plt

# %%
x1 = 2
x2 = x1+1
x3 = x1
x4 = x1+1
x_val = [x1,x2,x3,x4]
y1 = 0
y2 = y1
y3 = y1+0.5
y4 = y1 +0.5
y_val = [y1,y2,y3,y4]

polygon1 =([
    (x_val[0],y_val[0]),
    (x_val[1],y_val[1]),
    (x_val[3],y_val[3]),
    (x_val[2],y_val[2])
])

# loop to close the shape
polygon1.append(polygon1[0])

x,y = zip(*polygon1)

plt.figure()
plt.plot(x, y, marker='o', c="green")
plt.plot((x[0],x[2]), (y[0],y[2]),linestyle='--')
plt.plot((x[1],x[3]), (y[1],y[3]),linestyle='--')

#by definition in rightangle parallelogram the half length of the
#diagonal is in fact the midle point 
X0 = (x[0]+x[2])/2
Y0 = (y[0]+y[2])/2
plt.plot(X0,Y0 ,marker='o',c='r', label='crossing point')
center = [X0,Y0]
#The surface in squear meters is calculated
#from the equation : A = b*h, where b= base and h= hight

#diagonal_of_polygon = ((x[0]+x[2])/2) * ((y[0]+y[2])/2)
base = x[1]-x[0]
hight =y[3]-y[0]

plt.title('Rightangle Parallelogram')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc='best')
plt.show()

print(f'The surface area in square meters is equal to A={base*hight} m^2 \n The coordinates of the four corner points are :\n {polygon1[0:4]} \n The crossing point coordinates of the shape_s diagonals are : \n {center}')

# %%
# Ασκηση 2
# READY AS HELL 
import numpy as np

A = np.array([[1,2],[1.5,-1]])
B = np.array([[0],[5]])

x= np.dot(np.linalg.inv(A), B)

print (f'The result is \n x = \n {x}')

C = np.array([[11,3,0,1,2], [0,4,2,0,1], [3,2,7,1,0], [4,0,4,10,1], [2,5,1,3,14]])
D = np.array([[45],[30],[15],[20],[92]])

y= np.dot(np.linalg.inv(C),D)

variable_mtrx =[].append(y)
print (f'The result is \n x = \n {y}')

#%%
#Ασκηση 3

import numpy as np

X = np.array([[1,2,3],[4,5,6],[7,8,9]])
Y = np.array([[-0.1,-0.2,-0.3],[3,10,2],[4,2,0.5]])

x_vect = np.array([[1],[3],[4]])

#β) ερωτημα

dot_product = np.dot(X, Y)

#γ) ερωτημα

x_times_y = np.cross(X, Y)

#δ) ερώτημα

vect_dot_product = np.dot(X, x_vect)

# %%
# Ασκηση 4
def merge(L, left, middle, right):
    lcopy = L[left:middle + 1]
    rcopy = L[middle + 1:right + 1]
    i = j = 0; k = left
    while i < len(lcopy) and j < len(rcopy):
        if lcopy[i] < rcopy[j]:
            L[k] = lcopy[i]; i += 1
        else:
            L[k] = rcopy[j]; j += 1
        k += 1
    while i < len(lcopy):
        L[k] = lcopy[i]; i += 1; k += 1
    while j < len(rcopy):
        L[k] = rcopy[j]; j+= 1; k += 1


def merge_sort(L, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(L, left, middle)
        
        merge_sort(L, middle + 1, right)
        merge(L, left, middle, right)

    return L


The_list =  [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27,43, 
34, 46, 40]

copy_ = The_list.copy()

merge_sort(The_list, 0, len(The_list) - 1)

#%%
def recurcive_call (times_to_repeat, L):
    if times_to_repeat ==3:
        return L
    if times_to_repeat<3:
        recurcive_call(times_to_repeat+1, merge_sort(L, 0, len(L) - 1))
        print(L)

Rec_call = recurcive_call(0, The_list)
# %%
