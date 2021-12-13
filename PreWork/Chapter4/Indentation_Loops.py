


magicians = ['alice', 'david', 'carolina']
for magician in magicians: 
    print(magician)

#indent print and then undo the indent on line 12. Notice the difference in the output
#if line 12 isnt indented then everything prints bunched up, if its indented it prints correctly with space
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")

#this will cause an error because the print function doesnt belong to the line above it. 
#message = "Hello Python world!" 
#   print(message)



magicians = ['alice', 'david', 'carolina']
for magician in magicians:
       print(magician.title() + ", that was a great trick!")
       print("I can't wait to see your next trick, " + magician.title() + ".\n")
       print("Thank you everyone, that was a great magic show!")



# without the colon, the interpreter prints an error that the colon is expected
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians
print(magician)