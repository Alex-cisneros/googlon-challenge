

def foo_letter(letter):
    return letter in ['u', 'd', 'x', 's', 'm', 'p', 'f']


def bar_letter(letter):
    return not foo_letter(letter)


def preposition(word):
    if len(word) !=6 or 'u' in word or bar_letter(word[-1]):
        return False
    return True

def verb(word):
    if len(word) < 6 or foo_letter(word[-1]):
        return False
    return True

def verb_subjunctive(word):
    return verb(word) and bar_letter(word[0])



def googlon_sort(words):
    googlon_to_english = {"s": "a","x": "b","o": "c","c": "d","q": "e","n": "f","m": "g","w": "h","p": "i","f": "j","y": "k","h": "l","e": "m","l": "n","j": "o","r": "p","d": "q","g": "r","u": "s","i": "t"}
    set_words=set(words)
    return sorted(set_words, key=lambda word: "".join(googlon_to_english[char] for char in word))




def number_converter(word):
    googlon_to_numbers ={"s": 0,"x": 1,"o": 2,"c": 3,"q": 4,"n": 5,"m": 6,"w": 7,"p": 8,"f": 9,"y": 10,"h": 11,"e": 12,"l": 13,"j": 14,"r": 15,"d": 16,"g": 17,"u": 18,"i": 19}
    number = 0
    base = 1
    for character in word:
        number += googlon_to_numbers[character] * base
        base *= 20

    return number


def pretty_number(word):
    number = number_converter(word=word)
    return number >= 81827 and number % 3 == 0


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().split()



def count_total(words, fun):
    return len(set(list(filter(lambda word: fun(word), words))))







