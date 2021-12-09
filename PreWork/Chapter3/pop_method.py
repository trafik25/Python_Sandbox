

motorcycles = ['yamaha', 'ducati', 'harley', 'triumph ']
print(motorcycles)


#pop method removes the last item in a list
#this comes in handy with chronological lists for items purchased
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)


lastowned = motorcycles.pop()
print("The Last motorcycle I owned was a " + lastowned.title() + '.')




shopping = ['Nordstom', 'GAP', 'BR', 'Kmart']
print(shopping)

lastitem = shopping.pop()
print("The last place I went shopping was " + lastitem.title() + '.')

