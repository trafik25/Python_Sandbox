

#Dictonaries store info on people or things
#A dictionary in Python is a collection of key-value pairs. Each key is connected to a value
# dictionaries are wrapped in braces { }
# Every key is connected to its value by a colon,

car_0 = {'color': 'grey', 'trim_package': 'SL', 'engine': '5.5' }
print(car_0['color'])
print(car_0['trim_package'])
print(car_0['engine'])

#accessing a key
#This prints the key value of color only
car_0 = {'color': 'grey', 'trim_package': 'SL', 'engine': '5.5' }
print(car_0['color'])

#You can have an unlimited number of key-value pairs in a dictionary.

# FORMAT
# Var = {'KEY', 'VALUE': 'KEY', 'VALUE': 'KEY', 'VALUE':}
# print(key['value'])

car_0 = {'color': 'grey', 'trim_package': 'SL', 'engine': '5.5' }

new_car = car_0['engine']
print("This car has a " + str(new_car) + " liter engine in it.")
new_car_color = car_0['color']
print("This car comes with a " + str(new_car_color) + " color package.")