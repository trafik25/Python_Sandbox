

fav_lang = { 
        'Steph': 'C#',
        'Rob': 'python',
        'Jeff': 'HTML',
        'Sara': 'CSS',
        'John': 'cobol',
}

bestfriends = ['Steph', 'Rob']

for name, lang in fav_lang.items():
    print(name + ',' + " hey I see your fav language is " + lang)
    if name in bestfriends:
        print("Hey that's my best bud, they're fav language is " + lang)



