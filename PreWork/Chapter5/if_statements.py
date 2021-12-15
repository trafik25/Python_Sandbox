
##IF STATEMENTS
#Imagine you have a list of cars and you want to print out the name of each car. 


cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_toppings = ['mushrooms', 'onions', 'pineapple']
for topping in requested_toppings:
    if topping == 'tuna':
        print(topping.title())
    else:
        print(topping.upper())

my_cars = ['bmw', 'toyota', 'ferrari', 'pugeot', 'nissan']
for car in cars:
    if car == 'ferrari':
        print("That's a fancy car!")
    else:
        print("The car was too expensive")


banned_users = ['Tori', 'Larry', 'Juan', 'Marco']
for user in banned_users:
    if user == 'Larry':
        print("You are banned")
    else:
        print("You may continue playing!")

        