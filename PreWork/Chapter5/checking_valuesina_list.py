

#Checking Whether a Value Is in a List
#For example, you might want to check whether a new username 
# already exists in a list of current usernames


#CLI ONLY

#   requested_toppings = ['mushrooms', 'onions', 'pineapple'] 
#   'mushrooms' in requested_toppings
#True
#   'pepperoni' in requested_toppings
#False

#Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", You can post a response if you want")






#Pizza App  (if it has pepperoni add to order, if it has extra topping, add surcharge)
pizza_toppings = ['Pepperoni', 'Ham', 'Bacon', 'pineapple', 'hamburger', 'cheese', 'banana peppers', 'chilis', 'avocado']


for toppings in pizza_toppings: 

    if  toppings == 'banana peppers':
        print("There is a $2.00 surcharge for this topping.")
    elif toppings == 'chilis':
        print("There is a $2.00 surcharge for this topping.")
    elif toppings == 'avocado':
        print("There is a $2.00 surcharge for this topping.")
    if toppings == 'Pepperoni':
        print("This item has been added to your cart")
    elif toppings == 'Ham':
        print("This item has been added to your cart")
    elif toppings == 'Bacon':
        print("This item has been added to your cart")
    elif toppings == 'hamburger':
        print("This item has been added to your cart")
    elif toppings == 'cheese':
        print("This item has been added to your cart")
