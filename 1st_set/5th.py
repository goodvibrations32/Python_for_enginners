# password generator with chosen symbols from aveliable 
# to meet the requirements
# 

#%%
from ntpath import join
import secrets
import string
import random

S_letters = 3
S_digits = 5
S_symbols = 2
list_of_symbols = ('∗','%','@','$','(',')','[',']', '?', '#')

ran = "".join(random.choices(string.ascii_lowercase, k= S_letters)+ random.choices(string.digits, k=S_digits)+ random.choices(list_of_symbols, k=S_symbols))
password =''.join( random.sample(ran, k=10))

print (password)



# %%
