import string

sentence = "I am@Python@senior^pomidor"


list_with_words = sentence.split()
new_list = []

for word in list_with_words:
    if not word in string.punctuation:
        new_list.append(word)

#a = map(string, sentence, word, list_with_words)
#print(list(a))
#map filter только для чисел юзабельны? не до конца понял их в отличии от генератора список

nl = [word for word in list_with_words if not word in string.punctuation ]
print(nl)