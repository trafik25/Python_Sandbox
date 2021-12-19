
#This is an empty dictionary
#WHY USE THIS?? 


#Typically, you’ll use empty dictionaries when storing user-supplied data in a dictionary or 
# when you write code that generates a large number of key-value pairs automatically.

###EMPTY 
alien_0 = { }


alien_0['color'] = 'green'
alien_0['points'] = 30
alien_0['shape'] = 'square'
alien_0['x_position'] = 'moon'
alien_0['y_position']= 40

new_color = alien_0['color']
new_location = alien_0['x_position']
#These both do the same thing 
#one calls from the dictionary, one calls from the var
print("The " + (new_color) + " alien is now on the " + (new_location))
print("The " + alien_0['color'] + " alien is now on the " + alien_0['x_position'])


