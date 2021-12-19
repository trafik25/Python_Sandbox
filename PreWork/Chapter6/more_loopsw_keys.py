

fav_lang = { 
        'Steph': 'C#',
        'Rob': 'python',
        'Jeff': 'HTML',
        'Sara': 'CSS',
        'John': 'cobol',
}

bestfriends = ['Steph', 'Rob']

for name, lang in fav_lang.items():
    #print(name + ',' + " hey I see your fav language is " + lang)
    if name in bestfriends == 'Rob':
        print("Hi Rob, how is it going? ")

if 'erin' not in fav_lang.keys():
    print("Hey Erin take the poll!")

