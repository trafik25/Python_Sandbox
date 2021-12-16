
#Alien color 1
#passes
alien_color = 'blue'

if  alien_color == 'green':
    print("You just earned 5 points")
else:
    alien_color = 'blue'
    print("You just earned 10 pts")

#fails - simple fail -- no output because red isnt an option
alien_color = 'red'

if  alien_color == 'green':
    print("You just earned 5 points")

#fail complex fail -- fails because red is also not an option but the elif statement stops the code from running
alien_color = 'red'

if  alien_color == 'green':
    print("You just earned 5 points")

elif alien_color == 'purple':
    print("You earned 25 pts")

#green alien
alien_color = 'green'

if  alien_color == 'green':
    print("You just earned 5 points")
elif alien_color == 'yellow':
    print("You just earned 10 pts")
elif alien_color == 'red':
    print("You just earned 15 pts")
else:
    alien_color = 'orange'
    print("You just earned 50 pts")


#yellow alien
alien_color = 'yellow'

if  alien_color == 'green':
    print("You just earned 5 points")
elif alien_color == 'yellow':
    print("You just earned 10 pts")
elif alien_color == 'red':
    print("You just earned 15 pts")
else:
    alien_color = 'orange'
    print("You just earned 50 pts")


#red alien
alien_color = 'red'

if  alien_color == 'green':
    print("You just earned 5 points")
elif alien_color == 'yellow':
    print("You just earned 10 pts")
elif alien_color == 'red':
    print("You just earned 15 pts")
else:
    alien_color = 'orange'
    print("You just earned 50 pts")

#missing color alien
alien_color = 'tan'

if  alien_color == 'green':
    print("You just earned 5 points")
elif alien_color == 'yellow':
    print("You just earned 10 pts")
elif alien_color == 'red':
    print("You just earned 15 pts")
else:
    alien_color = 'blue'
    print("You just earned 50 pts")


