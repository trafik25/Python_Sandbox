

#Boolean can be two things (binary operator) it can be on/off, yes or no, true or false

#0 is always false, everything else is true
print(bool(0))
print(bool(""))  # empty string always false
print(bool(" trs"))  #occupied string is always true
print(bool([1,2]))  # occupied list is always true
print(bool([ ]))  # empty list is always false

#boolean expressions have operators
# > greater than 
# < less than 
# >= 
# ==  equal to
# != not equal to

print("dog" == "cat")
print("dog" == "dog")
print(4 > 8)

x = 3
print(5 < x < 20)  # 10 is betwen 5 and 20, 3 is not

letter = "c"
print(ord("b"))
print(letter > "a")

letter =  8
if True:
    print("Number is less than 8")


name = "Destiny's Child"
if name == "Destiny's Child":
    print("Say my name, say my name", end= " ")
print("If no one is around you", end=" ")
if name:
    print("say baby I love you", end= " ")
else:
    print("If you aint running game", end = " ")

x = 5
i = "5"
if x == i:
    print("This is right")