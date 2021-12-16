#Checking for Special Items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
       print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")



requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry but we are all out of green peppers right now")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")




cars = ['BMW', "Audi", "Tesla", 'Chevy']

for car in cars:
    if car == 'Tesla':
        print("\nSorry, but we are currently not running specials for " + cars[2] + " right now")
    if car == 'BMW':
        print("\nCurrent specials for " + cars[0] + " include $1000 off sticker price")
    elif car == 'Chevy':
        print("\nCurrent specials for " + cars[3] + " include $3500 off sticker price")
    elif car == 'Audi':
        print("\nCurrent specials for " + cars[1] + " include $3000 off sticker price")



