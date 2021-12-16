

##Multi line ELIF Statements 

car = 'Acura'

if car == 'audi':
    price = 40000
elif car == 'BMW':
    price = 55000
elif car == 'Acura':
    price = 43556
else:
    price = 35000
print("The price of this" + ' ' + (car) + " is" + ' $' + str(price) + '.')



###problem
age = 64
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65: price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")




#Python does not require an else block at the end of an if-elif chain. 
age = 64
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65: price = 10
elif age >= 65: price = 5

print("Your admission cost is $" + str(price) + ".")

requested_toppings = ['mushrooms', 'extra cheese']
#if you add elif to this block it stops at that value because Python only reads up to the if statement
if 'mushrooms' in requested_toppings:
    print("adding mushrooms")
elif 'extra cheese' in requested_toppings:
    print("adding extra cheese")
if 'pepperoni' in requested_toppings:
    print("adding pepperoni")
print("\nWe are building you pizza!")









