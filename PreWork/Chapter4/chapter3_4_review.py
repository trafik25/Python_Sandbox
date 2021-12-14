
#CHAPTER 3 REVIEW
#********************************LISTS********************************

# a simple list prints as it is displayed
bikes = ['cannondale', 'trek', 'specialized', 'giant' ]
print(bikes)

#ACCESS ALL elements within the list is easy
# call the bikes list and the position using brackets []
bikes = ['cannondale', 'trek', 'specialized', 'giant' ]
print(bikes[0])

#add TITLECASE to capitalize all your list elements
bikes = ['cannondale', 'trek', 'specialized', 'giant' ]
print(bikes[0].title())

#Accessing the LAST item in the list -1 will access GIANT 
bikes = ['cannondale', 'trek', 'specialized', 'giant' ]
print(bikes[-1])

#Creating a STRING statement and placing in that string one of the elements
bikes = ['cannondale', 'trek', 'specialized', 'giant' ]
print("My first bike was a, " + bikes[0].title())

#********************************CHANGING, ADDING AND REMOVING ELEMENTS********************************
#CHANGING THE VALUE OF AN ITEM IN A LIST
bikes = ['cannondale', 'trek', 'specialized', 'giant' ]

bikes[1] = 'schwinn'
print(bikes)

#ADDING elements to a list
bikes = ['cannondale', 'trek', 'specialized', 'giant' ]

bikes.append('Peloton')
print(bikes)

#Creating an empty list and then ADDING elements to it

motorcycles = []
motorcycles.append('Yamaha')
motorcycles.append('Ducati')
motorcycles.append('Harley')

print(motorcycles)

#INSERTING Elements into a List, the element STRIKER is inserted at 0
bikes = ['cannondale', 'trek', 'specialized', 'giant' ]
bikes.insert(0,'Striker')
print(bikes)

#Removing Elements from a List
#use a bracket for DEL statement and specify the position of the element to be deleted
bikes = ['cannondale', 'trek', 'specialized', 'giant' ]
del bikes[0]
print(bikes)

#removing an Item Using the pop() Method
#Giant was POPPED from the list and stored as "popped_bikes" variable
bikes = ['cannondale', 'trek', 'specialized', 'giant' ]
popped_bikes = bikes.pop()
print(bikes)
print(popped_bikes)

#Pop method chooses a random value every time, you just change the variable name
popped_bikes = bikes.pop()
print("My last owned bike was a" + ' ' + popped_bikes.title() + ".")

lastbike = bikes.pop()
print("My last owned bike was a" + ' ' + lastbike.title() + ".")

favbike = bikes.pop()
print("My last owned bike was a" + ' ' + favbike.title() + ".")

#REMOVING an Item by Value
bikes = ['cannondale', 'trek', 'specialized', 'giant' ]
bikes.remove('trek')
print(bikes)

#add the list
#create a var with a value from the list
#remove it the called var
#print the list
#print what you want the output to be 
bikes = ['cannondale', 'trek', 'specialized', 'giant' ]
too_expensive = 'trek'
bikes.remove(too_expensive)
print(bikes)
print("\nI cannot afford a" + ' ' + too_expensive.title() + ' ' + "because it is too expensive" + '.')

#organizing a List with SORT
