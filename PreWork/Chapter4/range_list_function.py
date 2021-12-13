

#Many reasons exist to store a set of numbers. 
#For example, you’ll need to keep track of the positions of each character

for value in range(1,5):
    print(value)


#turn the range into a list using list()function
numbers = list(range(1,6))
print(numbers)

#first number is the starting point
#second number is the end number 
#3rd number is count by how many
#start at 4, go to 13, every 2 numbers from 4
even_numbers = list(range(4,13,2))
print(even_numbers)



squares = []                #create a list called squares
for value in range(1,11):     #for the value in range 1-10, remember 11 is not shown
    squares.append(value**2)  #append the next squared value to the list for 1-10
print(squares)