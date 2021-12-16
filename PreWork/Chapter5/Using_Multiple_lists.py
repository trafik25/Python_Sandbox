

#LIST 1
cars = ['BMW', 'Audi', 'Ferrari', 'Tesla','Chevy', 'Dodge', 'Toyota']
available_cars = ['BMW', 'Audi', 'AMC', 'Judy']  #needs a value that isnt in the first list DUH

for available_car in available_cars:
    if available_car in cars:
        print("That car is available at our location") 
    else:
        print("Sorry, but at this time we do not have that " + available_car + " in stock")
print("\nCome on in for a look anyways!")



####LIST 2
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")