#Index      0        1          2        3
foods = ['pizza', 'tacos', 'dim sum', 'sushi']  #foods are objects in my list

#listname [index]
for food in foods: 
    if food == 'dim sum': 
       continue   
    print(f"I like {food} because they are yummy")

#List the foods by my fav in order from fav to least fav
for food in foods: 
    if food == 'dim sum': 
       continue   
    print(f"I like {food} because they are yummy")


for index in range(len(foods)):
    print(index)
    print(foods[index])

#for index, food in enumerate(foods):

print(list(enumerate(foods)))
for index, food in enumerate(foods):
    print(f"My No {index + 1} food is {food.title()}")
    
######
foods = ['pizza', 'pizza' , 'tacos', 'dim sum', 'sushi']
for food in foods:
    if food == 'pizza':
        break
    print(food, end= ' ')




