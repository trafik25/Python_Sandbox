#Questions I got wrong reviewed


#Sorts with .reverse
#reverse sorts a list in reverse alphabetical order
list = ['Tom', 'Wayne', 'Bob', 'Charles']
list.sort(reverse=True)
print(list)


#Sorted
#sorted sorts by order of the list 
names = ['Tom', 'Wayne', 'Bob', 'Charles']
sorted(names)
print(names)


#append----Append adds whatever is in the parens no matter what is there, quotations or not, string or integer
names = ['Tom', 'Wayne', 'Bob', 'Charles']
names.append(4)
print(names)




#pop --pops the last value in a list
listpop = ['Tom', 'Wayne', 'Bob', 'Charles']
listpop =listpop.pop()
print(listpop)


listpop = ['Tom', 'Wayne', 'Bob']
listpop =listpop.pop()
print(listpop)




#FOR Statements ---------problem I missed 
#the value added in the new list is placed in front of the list 
mylist = ['Tom', 'Wayne', 'Bob', 'Charles']
new_list= ''  #This removed the quotes 
for list in mylist:
    new_list += list + " " #added a space between values
print(new_list)




#INDEX-ing values 
mylist = ['Tom', 'Wayne', 'Bob', 'Charles']
for index in mylist:
    print(index, end= ' ') #quotations is adding whatever is in there, so here its blank

mycars = ['Audi', 'bmw', 'chevy']
for cars in mycars:
    print(cars, end= ' ')



#Trying to Pass a string into the index--Range >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
mylist = ['Tom', 'Wayne', 'Bob', 'Charles']
my_string = " "
for index in range(len(mylist)):
    if index == 1:
        my_string  += "chillin with my homies"
    my_string[index] = "Tom"
print(my_string)


#isinstance () FUNCTION
#The isinstance() function returns True if the 
# specified object is of the specified type, otherwise False.
my_list = [1, 3.0, ["a", "b", ["A", "B", "C"] ,"d"], "John"]
for member in my_list: 
    if isinstance(member, list):
        for m in member:
            if isinstance(m, list):
             print(m, end=" ")


#break function
my_list = ['bmw', 'audi', 'toyota', 'ferrari']
for cars in my_list:
    if cars == "bmw":
        break   #nothing is printed because we BREAK at the first value in the index
        print(cars, end= " ")


