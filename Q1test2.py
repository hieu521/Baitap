
import string

def my_capword(sentence):
    sentence = sentence.split()
    sentence = ' '.join(word[0].upper() + word[1:].lower() for word in sentence)
    return sentence

sentence ="hELLO wORLD"


print(my_capword(sentence))