


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(language.title())



# keys come first in the list
# values are the information on the key

#To see each language chosen without repetition, we can use a set.
#Set identifies the topics and removes dupes