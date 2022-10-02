from alice import cleanup_text
from symmetric_digraphs import n_graphs

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_word_frequencies():
    with open('all_words.txt') as file:
        word_frequencies = {}
        
        lines = [line.rstrip() for line in file.readlines()]
        for line in lines:
            [word, frequency] = line.split(',')

            for c in ALPHABET:
                word = word.replace(f"{c}{c}", f"{c}X{c}")
            
            word = word.replace("J", "I")

            word_frequencies[word] = int(frequency)

        return word_frequencies

def calculate_percent_of_quadgraphs_which_are_words():
    words = get_word_frequencies().keys()

    text = cleanup_text(open("alice.txt", encoding="utf8").read())
    quadgraphs = n_graphs(text, 4)

    word_quadgraphs = 0

    for quadgraph in quadgraphs:
        if quadgraph in words:
            word_quadgraphs += 1
    
    return float(word_quadgraphs) / float(len(quadgraphs))

# print(calculate_percent_of_quadgraphs_which_are_words())
   