f = open("alice.txt", "r")
text = f.read()

LENGTH = 6
OUTPUT_LIST = False

alphabet_text = ""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Remove all special characters and capitalize
for c in text:
    if c.capitalize() in alphabet:
        alphabet_text += c.capitalize()
    elif c == ",":
        alphabet_text += "COMXMA"
    elif c == ".":
        alphabet_text += "DOT"

# Remove "Alice" because it ended up being a really common word
alphabet_text = alphabet_text.replace("ALICE", "")

# Replace all instances of double letters
for c in alphabet:
    alphabet_text = alphabet_text.replace(f"{c}{c}", f"{c}X{c}")

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