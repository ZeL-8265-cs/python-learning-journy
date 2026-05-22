#! python3
# Mad libs - Create a file that people can add random vocabularies to create a silly sentence

import os, pyinputplus as pyip

path = os.path.join(os.path.expanduser("~"), "Desktop", "sentence.txt")
text = 'A ADJECTIVE panda tried to VERB1 in a NOUN1 , but a confused NOUN2 stopped everything and started to VERB2 for no reason.'
with open(path, 'w') as f:
    f.write(text)

# open and read the file
def read_sentence():
    madLibFile = open(path, 'r')
    sentence = madLibFile.read()
    madLibFile.close()
    return sentence

def get_input():
    adjective = pyip.inputStr(prompt="Enter a adjective: ")
    verb1 = pyip.inputStr(prompt="Enter a first verb: ")
    noun1 = pyip.inputStr(prompt="Enter a first noun: ")
    noun2 = pyip.inputStr(prompt="Enter a second noun: ")
    verb2 = pyip.inputStr(prompt="Enter a second verb: ")
    return [adjective, verb1, noun1, noun2, verb2]

def replace_word(text,inputWord):
    words = text.split(' ')
    new_words = []
    for word in words:
        if word == 'ADJECTIVE':
            new_words.append(inputWord[0])
        elif word == 'NOUN1':
            new_words.append(inputWord[2])
        elif word == 'VERB1':
            new_words.append(inputWord[1])
        elif word == 'NOUN2':
            new_words.append(inputWord[3])
        elif word == 'VERB2':
            new_words.append(inputWord[4])
        else:
            new_words.append(word)
    return ' '.join(new_words)

# main loop
while True:
    text = read_sentence()
    inputs = get_input()
    result = replace_word(text,inputs)
    print(f'{result}\n')
    # write the sentence into story file
    madLibFile = open(path, 'w')
    madLibFile.write(result)
    madLibFile.close()

    print('Your story has been saved to story.txt on Desktop.\n')

    print('Play again? (Yes/No)')
    response = pyip.inputChoice(["Yes", "No"], prompt = 'Please enter Yes or No')
    if response == 'No':
        break

