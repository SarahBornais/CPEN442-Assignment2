from typing import Counter

from alice import cleanup_text
from symmetric_digraphs import n_graphs, get_ciphertext
from words import get_word_frequencies
from simulated_annealing import scoring_agent, simulated_annealing_agent

class char_frequency_scoring_agent(scoring_agent):
    def __init__(self, ciphertext: str, sample_plaintext) -> None:
        super().__init__(ciphertext)
        self.char_frequencies = Counter(sample_plaintext)

    def calculate_score_from_plaintext(self, plaintext, _) -> float:
        plaintext_frequencies = Counter(plaintext)
        sum_of_differences_squared = 0

        for (char, char_frequency) in self.char_frequencies.items():
            plaintext_frequency = plaintext_frequencies.get(char, 0)
            sum_of_differences_squared += pow(plaintext_frequency - char_frequency, 2)

        return (1.0 / sum_of_differences_squared) * 1e8

class quadgraph_word_frequency_scoring_agent(scoring_agent):
    def __init__(self, ciphertext: str) -> None:
        super().__init__(ciphertext)
        self.word_frequencies = get_word_frequencies()

    def calculate_score_from_plaintext(self, plaintext, verbose) -> float:
        quadgraphs = n_graphs(plaintext, 4)
        counter = Counter()

        for quadgraph in quadgraphs:
            frequency =  self.word_frequencies.get(quadgraph, 0)
            if frequency > 1000: counter.update([quadgraph])

        score = 0

        for (word, frequency) in counter.most_common():
            if frequency >= 2: 
                score += 1
                if (verbose): print(word + ", " + str(frequency))
    
        return score

def run_simulated_annealing(ciphertext):
    alice_file = open("alice.txt", "r", encoding="utf8")
    alice_text = cleanup_text(alice_file.read())
    scoring_agent = quadgraph_word_frequency_scoring_agent(ciphertext)

    # remove duplicates
    ciphertext_digraphs = list(set(n_graphs(ciphertext, 2)))
    alice_digraphs = list(set(n_graphs(alice_text, 2)))

    agent = simulated_annealing_agent(ciphertext_digraphs, alice_digraphs, scoring_agent)
    agent.step(max_steps=10000, print_text=False, print_scores=False)

    if (agent.scoring_agent.calculate_score(agent.mappings) > 0):
        agent.print_results()

ciphertext = get_ciphertext()

while True:
    run_simulated_annealing(ciphertext)