

fav_numbers = { 
        'Steph': 5, #use str function because you are converting a string to an int value
        'Rob': 10,
        'Jeff': 15,
        'Sylvia': 0,
        'John': 45,
}


for name, number in fav_numbers.items():
    print(name + "'s" + " favorite number is " + str(number))


#Looping Through All the Keys in a Dictionary
fav_sports = {
        'John': 'hockey',
        'Laura': 'golf',
        'Thomas': 'tennis',
        'Sara': 'skiing',
}

#to print both values you need to separate with  comma
for name, sports in fav_sports.items():
    print(name + "'s" + " fav sport is " + sports)

#to print the first value you just call the name var
for name in fav_sports.keys():
    print(name)