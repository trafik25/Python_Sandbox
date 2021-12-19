

fav_numbers = { 
        'Steph': 5, #use str function because you are converting a string to an int value
        'Rob': 10,
        'Jeff': 15,
        'Sylvia': 0,
        'John': 45,
}


for name, number in fav_numbers.items():
    print(name + "'s" + " favorite number is " + str(number))

