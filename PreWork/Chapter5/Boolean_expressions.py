

#A Boolean value is either True or False
#Boolean values are often used to keep track of certain conditions, such as 
# whether a game is running or whether a user can edit certain content on a website:



##BOOLEAN EXPRESSION
a = 200
b = 337

if b != a:
  print("b is greater than a")
else:
  print("b is not greater than a") 



###>>>>>>>>>>>>>PROBLEM
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'bmw')



###>>>>>>>>>>>>>PROBLEM
employees = ['Susan', 'Tolly', 'Thomas', 'Frank', 'Jared', 'Tony']
for people in employees:
    if people == 'Thomas':
        print(people.title() + ' ' + "is our best employee!")
    else:
        print("No title found")

