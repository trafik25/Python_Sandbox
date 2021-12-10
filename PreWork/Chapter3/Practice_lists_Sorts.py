


#sort is IN PLACE 
# .sort only works on lists 
mystring = ['BMW', 'Ford', 'Tesla', 'Ferrari']
print(mystring.sort())
print(mystring.sort(reverse=True))
print(mystring) 


#sorted is OUT of place
mystring = ['BMW', 'Ford', 'Tesla', 'Ferrari']
print(sorted(mystring))
print(mystring)
mystring = sorted(mystring)
print(mystring)

