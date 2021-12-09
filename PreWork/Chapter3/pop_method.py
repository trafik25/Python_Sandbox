

motorcycles = ['yamaha', 'ducati', 'harley', 'triumph ']
print(motorcycles)


#pop method removes (does not DELETE from list) the last item in a list
#this comes in handy with chronological lists for items purchased
list_motorcycles = motorcycles.pop()
print(motorcycles)
print(list_motorcycles)


lastowned = motorcycles.pop()
print("The Last motorcycle I owned was a " + lastowned.title() + '.')



##Practice
shopping = ['Nordstom', 'GAP', 'BR', 'Kmart']
print(shopping)

lastitem = shopping.pop()
print("The last place I went shopping was " + lastitem.title() + '.')

