

fav_lang = { 
        'Steph': 'C',
        'Rob': 'python',
        'Jeff': 'HTML',
        'Sara': 'CSS',
        'John': 'cobol',
}

friends = ['Jacob', 'Jen']
best_friends = ['Rob', 'Jeff']
for name in fav_lang.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name + "I see your fav lanugage is " + fav_lang[name] + "!")
    elif name in best_friends:
        print("Hey these are my best friends " + name + " they love " + fav_lang[name])
    else:
        print("These are not my friends")
print("Everyone I know loves programming")
