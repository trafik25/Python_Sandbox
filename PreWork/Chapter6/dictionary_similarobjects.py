
#A simple poll
favorite_languages = {
       'jen':     'python',
       'sarah':   'C#',
       'edward':  'ruby',
       'phil':    'python',
       }
print("Sarah's fav programming language is " + favorite_languages['sarah'].title() + "!")

person = { 
        'firstname': 'Ron',
        'lastname': 'Howard',
        'phone_number': 2068527023 ,
        'location': 'Whidbey Island' , 
        'height' : 75,
        'weight': 200,
        'eyes' : 'blue',
        'occupation': 'loan officer',
}
print("My brothers name is " + person['firstname'] + ' ' + person['lastname'] + " his occupation is " + person['occupation'])


fav_numbers = { 
        'Steph': 5, 
        'Rob': 10,
        'Jeff': 15,
        'Sylvia': 0,
        'John': 45,
}

print("Steph's fav number is " + str(fav_numbers['Steph']))
print("Rob's fav number is " + str(fav_numbers['Rob']))
print("Jeff's fav number is " + str(fav_numbers['Jeff']))
print("Sylvia's fav number is " + str(fav_numbers['Sylvia']))
print("John's fav number is " + str(fav_numbers['John']))