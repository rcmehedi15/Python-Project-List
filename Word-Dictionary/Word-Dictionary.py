from PyDictionary import PyDictionary

dictionary = PyDictionary()
while True:
    word = input("Enter your Word :")
    if word == "":
        break
print(dictionary.meanings(word))
