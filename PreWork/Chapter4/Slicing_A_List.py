

#print the players in the list at a certain position in the list 
players = ['Ophelia', 'Sophie', 'Todd', 'Jeremy', 'Eli']
print(players[0:1])

#print the values in the list from a certain index onward
players = ['Ophelia', 'Sophie', 'Todd', 'Jeremy', 'Eli']
print(players[2:])   #<---- Removed the 2nd value 



#return the values 3 indexes from the last value 
#start at Eli and work backwards
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])


#looping through a list of players
#print the players list from the end -4 values 
#Message and then print the names left by title
#ITS IN ORDER OF HOW YOU WANT IT TO APPEAR PRINTED OUT!!!
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are 2  players on my team:")
for player in players[:-4]:
    print(player.title())


#print the players from a certain position on the roster
#Here I am selecting players at position 1 through 3
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are 2  players on my team:")
for player in players[1:3]:
    print(player.title())


   