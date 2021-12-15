

#@The if-elif-else Chain


#######DATA below
#Admission for anyone under age 4 is free.
#Admission for anyone between the ages of 4 and 18 is $5.
#Admission for anyone age 18 or older is $10.

age = 25

if age <4:
    print("Your admission is free")
elif age < 18:
    print("Your admission is 5$")
else:
    print("Your admission is 10$")

age = 12


if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 25
print("Your admission today is $" + str(price) + '.')  ##returns a string version of the object 

