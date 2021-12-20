

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# REALISTIC EXAMPLE: Make an empty list for storing aliens.
aliens = []

# Make 15 green aliens using range().
for alien_number in range(15):
    new_alien = {'color': 'red', 'points': 15, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'red':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 20

# Show the first 5 aliens using a slice[:5]
for alien in aliens[:7]:
       print(alien)
print("...")

