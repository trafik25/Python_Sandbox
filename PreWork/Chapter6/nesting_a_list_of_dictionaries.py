

#you’ll want to store a set of dictionaries in a list or a list of items as a value in a dictionary

#create a dictionary of aliens
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

#create a list of those aliens
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)







# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))