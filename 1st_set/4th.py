# 
# α. Να γράψετε μια συνάρτηση, η οποία λέγεται compute_avg , 
# παίρνει ως όρισμα τρεις
# αριθμούς και ναεπιστρέφειτον μέσο όρο τους.
# 
# β. Ναγράψετε από μίασυνάρτηση, που να εκτελεί τις παρακάτω 
# μετατροπές μονάδων:
# 1. Βαθμοί Κελσίου (Celsius) σε Farhenheit.
# 2. Βαθμοί Farhenheit σε βαθμούς Κελσίου.
# 3. Hp σε Watt.
# 
# Για κάθε μία μετατροπή δώστε και ένα παράδειγμα σε 
# μορφοποιημένη μορφή. Π.χ., ‘100 
# degrees Celcius = 212 degrees Fahrenheit’.
# 

#%%
#Compute the average of a list of 3 numbers
import numpy as np

def compute_avg(x1,x2,x3):
    num_avg = np.average([x1,x2,x3])
    return num_avg

print (compute_avg(10,20,30))


# %%
#Celsius to Farhenheit
# source : https://www.metric-conversions.org/el/temperature/celsius-to-fahrenheit.htm
def cel_to_far (x):
    far = x* 1.8 + 32
    return far

print ('100 degrees Celcius =', cel_to_far(100),'degrees Farhenheit')


# %%
# Farhenheit to Celcius
# source : https://www.metric-conversions.org/temperature/fahrenheit-to-celsius.htm

def far_to_cel (x2):
    cel = (x2-32)/1.8
    return cel

print('212 degrees Farhenheit =', far_to_cel(212), 'degrees Celcius')



# %%
# I will examine metric Hp and Mechanic and  Hydraulic Hp convertion
# source :  https://www.rapidtables.com/convert/power/hp-to-watt.html

# Mechanic and Hydraulic Hp to Watts 1hp = 745.699872 W

def Hp_to_watt_mech(x_hp_mech):
    y_watt_mech = x_hp_mech *745.699 
    return y_watt_mech

print('Mechanic and hydraulic power convention: 10 Hp = ' ,Hp_to_watt_mech(10), 'Watts')


# Metric Hp to Watts 1 hp(M) = 735.49875 W

def Hp_to_watt_metric(x_hp_metr):
    y_watt_metr = x_hp_metr * 735.498
    return y_watt_metr

print('Metric units power convention: 10 Hp = ' ,Hp_to_watt_metric(10), 'Watts')


# %%
