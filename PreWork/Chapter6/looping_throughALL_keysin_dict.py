

#Looping Through All the Keys in a Dictionary
fav_sports = {
        'john': 'hockey',
        'laura': 'golf',
        'thomas': 'tennis',
        'sara': 'skiing',
}

for name in fav_sports.keys():
    print(name.title())





##EXAMPLE 2 Using the keys() method to work with a specific key(s)
fav_sports = {
        'john': 'hockey',
        'laura': 'golf',
        'thomas': 'tennis',
        'sara': 'skiing',
}


friends = ['john', 'laura']
for name in fav_sports.keys():
    print(name.title())

    if name in friends:
        print("Hi," + ' ' + name.title() + " I see your fav sport is " 
        + fav_sports[name].title())



