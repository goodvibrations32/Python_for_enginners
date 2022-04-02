"""
Αναζήτηση προκαθορισμένου στοιχείου σε λίστα

Εδώ μόλις βρεί κάποιο στοιχείο που εκπληρώνει 
τις προϋποθέσεις σταματά την αναζήτηση (for-loop)
και επιστρέφει αποτέλεσμα στην οθόνη αγνοόντας 
περισσότερα ίδια στοιχεία στη λίστα

"""
#%%

def lin_search_list(L, x):
    i=0
    SOME_LIST=[]
    while i < len(L) and i!= len(L):
        for e in L:
            if e==x:
                SOME_LIST.append(i)
                return i, SOME_LIST
            i += 1
        return None
    
    

L= [3,6,2,7,8,9111,59,100,2,11,141,167,3436,0,4,2]
x =2

print('The position of the number in the list is',lin_search_list(L, x))
# %%
"""
This approach search all the list and returnes the indexies 
of the numbers that are equal to x 
"""

INDICIES = [i for i,y in enumerate(L) if y==x ]
print(f'The positions of x in the list L are {INDICIES}')
# %%
