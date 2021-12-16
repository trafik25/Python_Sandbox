
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







