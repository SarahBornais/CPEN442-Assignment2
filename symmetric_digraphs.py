from typing import Counter
import functools

def get_ciphertext():
    f = open("input.txt", "r")
    return f.read()

def n_graphs(text, length):
    n_graphs = []
    for i in range(0, len(text) - length - 1, 2):
        n_graphs.append(text[i:i+length])
    return n_graphs

# taken directly from findfrequencies.py
def print_frequencies(frequencies):
    count = 0
    print("| ", end="")
    for item in sorted(frequencies.items(), key=lambda item: item[1], reverse=True):
        end = " | "
        if count > 100:
            break
        if (count + 1) % 10 == 0:
            end = " |\n| "
        print("{}: {:>5}".format(item[0], item[1]), end=end)
        count += 1

# returns a list of (('AB', frequency of 'AB'), ('BA', frequency of 'BA'))
def combine_symmetric_digraphs(digraph_frequencies):
    combined = []
    seen = set()
    for digraph, frequency in digraph_frequencies.items():
        reversed_digraph = digraph[::-1]

        if digraph in seen or reversed_digraph in seen:
            continue

        reversed_digraph_frequency = digraph_frequencies.get(reversed_digraph, 0)

        if (reversed_digraph_frequency > 0):
            combined.append(((digraph, frequency), (reversed_digraph, reversed_digraph_frequency)))
            seen.add(digraph)
            seen.add(reversed_digraph)

    return sorted(combined, key=functools.cmp_to_key(compated_combined_symmetric_digraphs))

# compares the sum of the two frequencies
def compated_combined_symmetric_digraphs(item1, item2):
    ((_, freqAB), (_, freqBA)) = item1
    ((_, freqCD), (_, freqDC)) = item2

    sum1 = freqAB + freqBA
    sum2 = freqCD + freqDC
    
    if sum1 < sum2: return 1
    elif sum1 > sum2: return -1
    else: return 0

def print_symmetric_digraphs():
    ciphertext = get_ciphertext()

    digraphs = n_graphs(ciphertext, 2)
    # print(digraphs)

    digraph_frequencies = dict(Counter(digraphs))
    # print(digraph_frequencies)      

    combined = combine_symmetric_digraphs(digraph_frequencies)
    for pair in combined:
        print(pair)

# print_symmetric_digraphs()