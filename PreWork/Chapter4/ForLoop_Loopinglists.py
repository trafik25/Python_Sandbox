


#When you want to do the same action with every item in a list, use FOR loop
#This line tells Python to pull a name from the list magicians, and store it in the variable magician
magicians = ['alice', 'david', 'carolina'] 
new_magician = ''
for wood in magicians:
    print(new_magician)


#why loops?
#For example, you might use a for loop to initialize 
# a game by running through a list of characters and displaying each character on the screen.

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(magician.title() + ',' + "that was an amazing trick" + "!")
    print("I can't wait to see the next trick that" + ' ' + magician.title() + ' ' + "performs" + "!" + ".\n")
print("Thank you everyone, that was a great magic show" + "!" )


