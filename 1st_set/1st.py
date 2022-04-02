
# 
# Να γράψετε ένα πρόγραμμα το οποίο θα τυπώνει το Ονοματεπώνυμο και τον AM σας με λατινικούς
# χαρακτήρες και θα αντιστρέφει την σειρά των χαρακτήρων του (string). Παράδειγμα: “Papadakis Manolis
# ΑΜ20000”, και το αναμενόμενο απότελεσμα (output) που θα εκτυπωθεί στην οθόνη θα είναι:
# “00002MA silonaM sikadapaP”.
# 
#%%
def reverce (txt):
    return txt[::-1]

txt  = "Torosian Nikolaos TM6220"
print(txt, reverce(txt))
# %%
