

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

#simple stats with python
#Finding the sum of all digits
digits = [1,2,3,4,5,6,434,232,34]
min(digits)
print(sum(digits))

#Finding the min digit
digits = [1,2,3,4,5,6,434,232,34]
min(digits)
print(min(digits))

#Finding the Max digit
digits = [1,2,3,4,5,6,434,232,34]
min(digits)
print(max(digits))

#LIST COMPREHENSIONS are an easier way to combine lists into one line of code 
#find the square of each number in the range 1-12
squares = [value**2 for value in range(1,12)]
print(squares)

#Slicing a List
#this requests the index of players X:X so 2:5 would be Tom - Jason
players = ['charles', 'mona', 'tom', 'charlie', 'jason']
print(players[2:5])

# This would list all the players from first to fifth
players = ['charles', 'mona', 'tom', 'charlie', 'jason']
print(players[:5])


# This would list all the players from index 3-5
players = ['charles', 'mona', 'tom', 'charlie', 'jason']
print(players[3:])

players = ['charles', 'mona', 'tom', 'charlie', 'jason']
print(players[3:])

players = ['charles', 'mona', 'tom', 'charlie', 'jason']
for index in range(2):
        print(players[index], end=" ")


