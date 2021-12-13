#index      0         1         2       3
foods = ['pizza', 'tacos', 'dim sum', 'sushi']
#list name [index]
print(foods[1])

#for PLACEHOLDER in THELISTWEWANT: 
    #code block goes here
    #COLONs specify a code block


for food in foods:
    if food == "dim sum": 
        continue   
    print(f"I like {food} because they are yummy!")


for index in range(len(foods)):
    print(index)
    print(foods[index])

print(list(enumerate(foods)))
for index, food in enumerate(foods):
    print(f"My No {index + 1} food is {food.title()}" )

#loop of the index
print(list(range(len(foods))))
print(len(foods))