


#A more complicated version
alien_0 = {'x_position': 25, 'y_position': 40, 'speed': 'medium'}
print("Original x_position " + str(alien_0['x_position']))

if alien_0['speed'] == 'fast':
    x_increment = 1
if alien_0['speed'] == 'slow':
    x_increment = 2
elif alien_0['speed'] == 'xfast':
    x_increment = 3
else:
    x_increment = 4

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("The new position: " + str(alien_0['x_position']))
