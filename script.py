from functions import *
import glob
path = "./files/"
files = glob.glob(path+"*.txt")



for file in files:

    print("\n")
    print("\n")

    print("***** Reading file " + file + "**************************")
    print("\n")
  
    words = read_file(file)
    print("***********total prepositions in text***************")
    prepositions=count_total(words,preposition)
    print(prepositions)


    print("*****************total verbs in text******************")
    verbs=count_total(words,verb)
    print(verbs)


    print("*************total verbs in subjunctive form in text*****************")
    subjunctive_verbs=count_total(words,verb_subjunctive)
    print(subjunctive_verbs)

    print("*******************order words list**********************")
    order_words = googlon_sort(words)
    for word in order_words:print(word)

    print("*************total Pretty numbers in text****************")
    pretty_numbers=count_total(words,pretty_number)
    print(pretty_numbers)
