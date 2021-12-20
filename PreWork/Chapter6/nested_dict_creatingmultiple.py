

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# REALISTIC EXAMPLE: Make an empty list for storing aliens.
aliens = []

# Make 15 green aliens using range().
for alien_number in range(15):
    new_alien = {'color': 'green', 'points': 15, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:4]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 20
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 35
    

# Show the first 5 aliens using a slice[:5]
for alien in aliens[:8]:
       print(alien)
print("...")

