

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

#Pizza App
pizza_toppings = ['Pepperoni', 'Ham', 'Bacon', 'pineapple', 'hamburger', 'cheese']
topping = ['banana peppers', 'chilis', 'avocado']



for topping in pizza_toppings:
    if topping == 'banana peppers':
        print("There is a $2.00 surcharge for this topping.")
    elif topping == 'chilis':
        print("There is a $2.00 surcharge for this topping.")
    elif topping == 'avocado':
        print("There is a $2.00 surcharge for this topping.")

    if pizza_toppings == 'Pepperoni':
        print("This item has been added to your cart")
    elif pizza_toppings == 'Ham':
        print("This item has been added to your cart")
    elif pizza_toppings == 'Bacon':
        print("This item has been added to your cart")
    elif pizza_toppings == 'hamburger':
        print("This item has been added to your cart")
    elif pizza_toppings == 'cheese':
        print("This item has been added to your cart")
