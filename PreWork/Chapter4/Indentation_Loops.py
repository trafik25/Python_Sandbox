


magicians = ['alice', 'david', 'carolina']
for magician in magicians: 
    print(magician)

#indent print and then undo the indent on line 12. Notice the difference in the output
#if line 12 isnt indented then everything prints bunched up, if its indented it prints correctly with space
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")