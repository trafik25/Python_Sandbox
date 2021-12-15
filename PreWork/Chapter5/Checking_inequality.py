#####Conditional tests
##if statement is an expression that can be evaluated 
# as True or False and is called a conditional test
#Equality is CASE Senstive in Python
# so Audi is not equal to audi 

#Checking for Inequality
#When you want to determine whether TWO VALUES ARE EQUAL, 
# you can combine an exclamation point and an equal sign (!=).

requested_topping = 'cheese' 

if requested_topping != 'mushrooms':
    print("No mushrooms please")

if requested_topping != 'anchovies':
    print("No anchovies please")

if requested_topping != 'cheese':
    print("No mushrooms please")   #This prints nothing because the variable is equal to cheese

## != IF TWO VALUES ARE EQUAL OR NOT
