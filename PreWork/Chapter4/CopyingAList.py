

# [:] This allows you to copy a list by removing the values
my_foods = ['pizza', 'falafel', 'carrots'] 
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)



#practice 
fav_players = ['lebron' , 'curry', 'magic']
friends_favplayers = fav_players[:]

print("My fav NBA players are:")
print(fav_players)

print("\nMy friend's favorite NBA players are:")
print(friends_favplayers)


#practice append and remove
fav_players = ['lebron' , 'curry', 'magic']
friends_favplayers = fav_players[:]

fav_players.remove('lebron')  #append has parens not
friends_favplayers.remove('curry')

print("My fav NBA players are:")
print(fav_players)

print("\nMy friend's favorite NBA players are:")
print(friends_favplayers)