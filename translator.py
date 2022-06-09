
WORDS = {
    'cat': 'Pisica',
    'fox': 'Volpe',
    'fish': 'Piste',
    'is': 'este',
    'hungry': 'foame',
}

def translate(english, dictionary):
    romanian = ''
    words = english.split()   # list of strings
    for w in words:
        if w in dictionary:
            romanian += dictionary[w] + " "
        #romanian += dictionary.get(w, '') + " "
    return romanian


r = translate("the cat is hungry", WORDS)
print(r)

