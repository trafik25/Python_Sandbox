

fav_numbers = { 
        'Steph': 5, #use str function because you are converting a string to an int value
        'Rob': 10,
        'Jeff': 15,
        'Sylvia': 0,
        'John': 45,
}


for name, number in fav_numbers.items():
    print(name + "'s" + " favorite number is " + str(number))




user_1 = {
        'name': 'Thomas',
        'height': "6'5",
        'weight': 215,
        'fav hobby': 'skiing'
}

for info, userdata in user_1.items():
    print("\n" + info)
    print("\n " + str(userdata))