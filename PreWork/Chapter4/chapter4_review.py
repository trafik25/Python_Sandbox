

#LISTS Review
#Looping through an entire List
magicians = ['Clara', 'Bob', 'Charlie']
for magician in magicians:
    print(magician)

cars = ['toyota', 'scion', 'Ferrari']
for car in cars: 
    print(car)    

cars = ['toyota', 'scion', 'Ferrari']
for car in cars: 
    print("My first car was a" + ' ' + car.title() + '!')    
    print(car.title() + ' ' + "is the best car ever!")    


#making numerical Lists
for value in range(1,5):
    print(value)


#Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

#Tells python to print only the even numbers from 0 to 12 counting by 2
evennumbers = list(range(0,12,2))
print(evennumbers)

#Using the range() function to find the square of any value from 1-15
squares = []
for value in range(1,15):
    square = value**2  #this is a temporary variable
    squares.append(square)
print(squares)

#easier way to write the code above 
squares = []
for value in range(1,15): #removing the temp variable
    squares.append(value**2)
print(squares)

