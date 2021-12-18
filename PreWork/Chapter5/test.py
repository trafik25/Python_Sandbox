

#The if statement keeps running until it finds the correct value and it prints that value
#here it is the second if
price = 100

if price > 100:
 print("price is greater than 100")

if price != 100:
  print("price is 100")

if price != 100:
    print("price is less than 100")

#Along with the if statement, the else condition can be optionally 
# used to define an alternate block of statements to be executed if 
# the boolean expression in the if condition evaluates to False. 

#else runs here because IF is false
price = 50

if price >= 100:
    print("price is greater than 100")
else:
    print("price is > than 100")

# The elif block is executed if the specified condition evaluates to True. 
price = 101

if price < 100:
    print("price is LESS than 100")
elif price == 100:
    print("price is 100")
    # this next line doesnt run because the 2nd value is true
elif price > 100:
    print("price is GREATER than 100")

# IF always runs
# else runs when IF is false
# elif runs when IF is true