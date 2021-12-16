

#Checking whether a list is empty
requested_toppings = []   

if requested_toppings: 
    for requested_topping in requested_toppings:
       print("Adding " + requested_topping + ".")
else:
    print("\nAre you sure you want a plain pizza?")


cars = [ ]

if cars:
    for car in cars:
        if car == 'BMW':
            print("\nCurrent specials for " + cars[0] + " include $1000 off sticker price")
        elif car == 'Chevy':
            print("\nCurrent specials for " + cars[3] + " include $3500 off sticker price")
        elif car == 'Audi':
            print("\nCurrent specials for " + cars[1] + " include $3000 off sticker price")

else:
    print("Sorry but we have no financing deals at this time")
