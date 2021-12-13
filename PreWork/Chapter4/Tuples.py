

#Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

dimension = (200,55)
print(dimension[0])
print(dimension[1])

#Looping Through All Values in a Tuple
dimensions = (200,55)
for dimension in dimensions: 
    print(dimension)



#Writing over a Tuple
dimensions = (200,55)
print("\nOriginal dimensions:")
for dimension in dimensions: 
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#Writing over the last tuple
dimensions = (750,354)
print("\nNew dimensions:")
for dimension in dimensions:
    print(dimension)
