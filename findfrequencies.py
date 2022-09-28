f = open("input.txt", "r")
input = f.read()

LENGTH = 6
OUTPUT_LIST = False

digraph_frequencies = {}

for i in range(0, len(input), 2):
    digraph = input[i:i+LENGTH]
    if digraph in digraph_frequencies.keys():
        digraph_frequencies[digraph] += 1
    else:
        digraph_frequencies[digraph] = 1

if OUTPUT_LIST:
    output = "["
    for item in sorted(digraph_frequencies.items(), key=lambda item: item[1], reverse=True):
        output += f"\"{item[0]}\", "
    output = output[:-2] + "]"
    print(output)
else:
    count = 0
    print("| ", end="")
    for item in sorted(digraph_frequencies.items(), key=lambda item: item[1], reverse=True):
        end = " | "
        if count > 100:
            break
        if (count + 1) % 10 == 0:
            end = " |\n| "
        print("{}: {:>5}".format(item[0], item[1]), end=end)
        count += 1