

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


