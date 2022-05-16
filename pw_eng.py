
#%%
from ntpath import join
import secrets
import string
import random

S_letters = 10
S_digits = 12
S_symbols = 8
list_of_symbols = ('∗','%','@','$','(',')','[',']', '?', '#')

ran = "".join(random.choices(string.ascii_lowercase, k= S_letters)+ random.choices(string.digits, k=S_digits)+ random.choices(string.punctuation, k=S_symbols))
password =''.join(random.sample(ran, k=30))

print (password)


# %%
