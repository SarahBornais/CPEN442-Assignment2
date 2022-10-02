f = open("alice.txt", encoding="utf-8")
text = f.read()

LENGTH = 6
OUTPUT_LIST = False

tmp_alphabet_text = ""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Remove all special characters and capitalize
for c in text:
    if c.capitalize() in alphabet:
        tmp_alphabet_text += c.capitalize()
    elif c == ",":
        tmp_alphabet_text += "COMMA"
    elif c == ".":
        tmp_alphabet_text += "DOT"

# Remove "Alice" because it ended up being a really common word
tmp_alphabet_text = tmp_alphabet_text.replace("ALICE", "")

alphabet_text = ""
for i in range(0, len(tmp_alphabet_text) - 1, 2):
    if (tmp_alphabet_text[i] == tmp_alphabet_text[i+1]):
        alphabet_text += tmp_alphabet_text[i]
        alphabet_text += "X"
        alphabet_text += tmp_alphabet_text[i+1]
    else:
        alphabet_text += tmp_alphabet_text[i]
        alphabet_text += tmp_alphabet_text[i+1]

if len(alphabet_text) % 2 != 0:
    alphabet_text += "X"

# Count digram frequencies
digram_frequencies = {}
for i in range(0, len(alphabet_text), 2):
    digram = alphabet_text[i:i+LENGTH]
    if digram in digram_frequencies.keys():
        digram_frequencies[digram] += 1
    else:
        digram_frequencies[digram] = 1

# Print frequency table
if OUTPUT_LIST:
    output = "["
    for item in sorted(digram_frequencies.items(), key=lambda item: item[1], reverse=True):
        output += f"\"{item[0]}\", "
    output = output[:-2] + "]"
    print(output)
else:
    count = 0
    print("| ", end="")
    for item in sorted(digram_frequencies.items(), key=lambda item: item[1], reverse=True):
        end = " | "
        if count > 100:
            break
        if (count + 1) % 10 == 0:
            end = " |\n| "
        print("{}: {:>5}".format(item[0], item[1]), end=end)
        count += 1

# get the most common quadgrams following CO MX MA
quadgram_frequencies = {}
for i in range(0, len(alphabet_text), 2):
    maybe_comxma = alphabet_text[i:i+6]
    if maybe_comxma == "COMXMA":
        print(alphabet_text[i:i+10])
        quadgram = alphabet_text[i+6:i+10]
        if quadgram in quadgram_frequencies.keys():
            quadgram_frequencies[quadgram] += 1
        else:
            quadgram_frequencies[quadgram] = 1

count = 0
print("| ", end="")
for item in sorted(quadgram_frequencies.items(), key=lambda item: item[1], reverse=True):
    end = " | "
    if count > 100:
        break
    if (count + 1) % 10 == 0:
        end = " |\n| "
    print("{}: {:>5}".format(item[0], item[1]), end=end)
    count += 1