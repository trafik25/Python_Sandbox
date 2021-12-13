
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











#WORKING WITH LISTS