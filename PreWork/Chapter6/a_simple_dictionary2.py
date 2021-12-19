

#A list is an ordered sequence of objects, whereas dictionaries are unordered sets. 
# However, the main difference is that items in dictionaries are accessed via keys 
# and not via their position


alien_0 = {'color': 'red', 'shape' : 'square' ,'points': 15}
alien_1 = {'color': 'blue', 'shape': 'round', 'points': 30 }
alien_2 = {'color': 'green', 'shape': 'rectangle', 'points': 60 }

new_color1 = alien_1['color']
new_points1 = alien_1['points']
new_shape1 = alien_1['shape']
new_color = alien_2['color']
new_points = alien_2['points']
new_shape = alien_2['shape']
print("You shot down the " + str(new_shape1) + " Alien! You just earned " + str(new_points1) + " points!")






