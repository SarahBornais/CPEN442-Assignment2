from abc import abstractmethod
from copy import deepcopy
from math import exp
from random import random
from typing import Counter, Tuple, Dict, List

from alice import cleanup_text
from symmetric_digraphs import n_graphs, get_ciphertext
from words import get_word_frequencies

INITIAL_TEMPERATURE = 0.1
TEMPERATURE_DURATION = 500
DECREMENT_FACTOR = 0.0005
MIN_TEMPERATURE = 0

class scoring_agent:
    def __init__(self, ciphertext: str) -> None:
        self.ciphertext = ciphertext

    def calculate_plaintext(self, digraph_mappings: Dict[str, str]) -> str:
        plaintext = ""

        for i in range(0, len(self.ciphertext) - 1, 2):
            ciphertext_digraph = self.ciphertext[i:i+2]
            plaintext += digraph_mappings[ciphertext_digraph]

        return plaintext
    
    def calculate_score(self, digraph_mappings: Dict[str, str ], verbose: bool=False) -> float:
        return self.calculate_score_from_plaintext(self.calculate_plaintext(digraph_mappings), verbose)

    @abstractmethod
    def calculate_score_from_plaintext(self, plaintext: str, verbose: bool) -> float:
        pass

class simulated_annealing_agent:
    def __init__(self, 
        source_strings: List[str], 
        destination_strings: List[str], 
        scoring_agent: scoring_agent) -> None:

        self.source_strings = source_strings
        self.destination_strings = destination_strings
        self.scoring_agent = scoring_agent
        self.temperature: float = INITIAL_TEMPERATURE
        self.mappings = {}
        self.step_count = 0
        
        # start with random mappings
        for source_string in source_strings:
            self.mappings[source_string] = self.get_random_untaken_destination()

        self.starting_score = self.scoring_agent.calculate_score(self.mappings)

    def get_random_untaken_destination(self):
        random_destination = self.destination_strings[int(random() * len(self.destination_strings))]

        while random_destination in self.mappings.values():
            random_destination = self.destination_strings[int(random() * len(self.destination_strings))]

        return random_destination

    # TODO: prune invalid mappings
    def get_random_mapping_changes(self) -> List[Tuple[str, str]]:
        if random() < 0.5:
            # swap two random mappings
            source_index_1 = int(random() * len(self.source_strings))

            source_index_2 = int(random() * len(self.source_strings))
            while source_index_1 != source_index_2:
                source_index_2 = int(random() * len(self.source_strings))

            source_1 = self.source_strings[source_index_1]
            source_2 = self.source_strings[source_index_2]

            destination_1 = self.mappings[source_1]
            destination_2 = self.mappings[source_2]

            return [(source_1, destination_2), (source_2, destination_1)]
        else:
            # choose a random source and assign it to a new, untaken destination
            source = self.source_strings[int(random() * len(self.source_strings))]
            destination = self.get_random_untaken_destination()

            return [(source, destination)]
        
    def substitue_mapping(_, mappings, mappings_to_substitue: List[Tuple[str, str]]) -> Dict[str, str]:
        new_mappings = deepcopy(mappings)

        for (source, destination) in mappings_to_substitue:
            new_mappings[source] = destination

        return new_mappings

    def calculate_move_probability(self, worse_score, current_score) -> float:
        return exp((worse_score - current_score) / self.temperature)

    def transform_mappings(self, current_mappings) -> Dict[str, str]:
        random_change_to_mappings = self.substitue_mapping(current_mappings, self.get_random_mapping_changes())

        current_score = self.scoring_agent.calculate_score(current_mappings)
        random_score = self.scoring_agent.calculate_score(random_change_to_mappings)

        difference = random_score - current_score

        # TODO: figure out scoring function callibration so that we don't have to be greedy
        if (difference >= 0):
            return random_change_to_mappings
        else:
            # move_probability = self.calculate_move_probability(random_score, current_score)
            # print("Move probability: " + str(move_probability) + " Difference: " + str(difference))
            # if (random() <= move_probability): return random_change_to_mappings
            # else: return current_mappings
            return current_mappings

    def step(self, max_steps: int, print_text: bool, print_scores: bool) -> None:
        for _ in range(0, max_steps):
            if print_scores: print(str(self.scoring_agent.calculate_score(self.mappings)))
            if print_text: print(self.scoring_agent.calculate_plaintext(self.mappings))

            self.mappings = self.transform_mappings(self.mappings)

            self.step_count += 1

            if (self.step_count % TEMPERATURE_DURATION == 0):
                self.temperature = self.temperature - DECREMENT_FACTOR

                if self.temperature <= MIN_TEMPERATURE:
                    return

    def print_results(self):
        # print("Total steps taken: " + str(self.step_count))
        # print("Starting score: " + str(self.starting_score))
        print("Ending score:   " + str(self.scoring_agent.calculate_score(self.mappings, verbose=True)))
        # print("Ending temperature: " + str(self.temperature))
        print("Plaintext: " + self.scoring_agent.calculate_plaintext(self.mappings))
        print("Mappings: " + str(self.mappings))
        # print("Plaintext frequencies: " + str(Counter(self.scoring_agent.calculate_plaintext(self.mappings))))
        print()