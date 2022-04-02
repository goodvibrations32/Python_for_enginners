# 
# Δίνονται οι παρακάτω λίστες: Names = [’Kostas’, ’Ioanna’, ’Manolis’, ’Eleni’,], και Tel_No =
# [207856, 218463, 188365, 181036]. Οι λίστες αυτές συνδυάζονται, έτσι ώστε το τηλέφωνο
# του Kostas να είναι 207856, της Ioanna να είναι 218463, κτλ. Να γράψετε ένα πρόγραμμα το
# οποίο συνδυάζει τις παραπάνω δύο λίστες σένα λεξικό. (Υπόδειξη! Τα λεξικά αποτελούνται
# από ζεύγη: κλειδί → τιμή. Σκεφτείτε στην προκειμένη περίπτωση ποια θα είναι τα κλειδιά και
# ποιες οι αντίστοιχες τιμές τους).
# Να γράψετε μια συνάρτηση με το όνομα People η οποία παίρνει ως όρισμα τoν α ρ ι θ μ ό τ ο υ
# τ η λ ε φ ώ ν ο υ καιεπιστρέφειτο αντίστοιχο όνομα. Τι εκτυπώνεται στην οθόνη κατά τις ακόλουθες
# περιπτώσεις;
# print(people(207856) == [’Kostas’])
# print(people(218463) == [’Ioanna’])
# print (people(181036) == [‘Manolis’])
# print people(123456) == []
# 
#%%

Names = ['Kostas', 'Ioanna', 'Manolis', 'Eleni']
Tel_no = [207856, 218463, 188365, 181036]

Phone_book =dict(zip(Tel_no,Names))

def People(via_no):
    x= Phone_book.get(via_no)

    return x

print (Phone_book, People(181036),People(207856) == ['Kostas'] , People(218463) == ['Ioanna'] , People(181036) == ['Manolis'], People(123456) == [], sep="\n")

# %%
#I have a problem with syntax and could not print the true resoults
#with the squear brackets on the values of the keys and 

print (Phone_book, People(181036),People(207856) == 'Kostas' , People(218463) == 'Ioanna' , People(181036) == 'Manolis', People(123456) == [], sep="\n")

# 
# """
# WRONG FUCKING WAY !!!! PYTHON POLICE ALERT
# print (People(207856) == 'Kostas')
# print (People(218463) == 'Ioanna')
# print (People(181036) == 'Manolis')
# print (People(123456) == [])
# """

# %%
