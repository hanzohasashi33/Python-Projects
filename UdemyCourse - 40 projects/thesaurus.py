from random import choice


print("Welcome to the thesaurus app\n")
print("Choose a word and i will give a synonym\n")
print("Here are the words in the thesaurus")
print("\t\t-hot")
print("\t\t-cold")
print("\t\t-happy")
print("\t\t-sad")

word = input("\nWhat word would you like a synonym for : ")
word = word.lower()

syn = {
    'hot' : ['balmy','summery','tropical','boiling','scorching'],
    'cold' : ['chilly','cool','freezing','frigid','tundra'],
    'happy' : ['content','cherry','merry','jovial','jocular'],
    'sad' : ['unhappy','downcast','miserable','glum','melancholy'],
}

print("A synonym for {} is {}.".format(word,choice(syn[word])))

boole = input("Would you like to see the whole thesaurus(y/n) : ")
if boole == 'y' :
    for i in syn :
        print("{} synonyms are : ".format(i))
        for j in syn[i] :
            print("\t\t-{}".format(j))
else :
    print("have a good day!")