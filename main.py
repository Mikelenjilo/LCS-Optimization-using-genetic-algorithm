from setup import setup
from lcs import LCS
from dataset_generation.helper_functions import generate_dataset
from dataset_generation.models.dataset_model import Dataset
from genetic_algorithm.models.selection_method_model import SelectionMethod
import time


def main():
    alphabets = [
        ['A', 'B'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
    ]

    nb_seqs = [
        10,
        100,
    ]

    seq_length = [10, 20]

    mutation_rates = [0.05, 0.10]
    max_gens = [100, 200]
    population_sizes = [100, 200]

    for i in alphabets:
        for j in nb_seqs:
            for z in seq_length:
                dataset: Dataset = generate_dataset(i, j, z)

                s_exact = time.process_time()
                lcs_exact = LCS.exact_method(dataset.sequences)
                if lcs_exact:
                    lcs_exact = lcs_exact[0][1]
                e_exact = time.process_time() - s_exact
                print(f"Exact method: {lcs_exact}, time: {e_exact}")

                s_ga = time.process_time()
                lcs_ga = \
                LCS.genetic_algorithm(chromosomes=dataset.sequences, population_size=200, mutation_rate=0.10, max_gens=200,
                                      selection_method=SelectionMethod.TOURNAMENT)[1]
                e_ga = time.process_time() - s_ga
                print(f"Genetic algorithm: {lcs_ga}, time: {e_ga}")

                print('----------------------------------------------')

    # start_time = time.process_time()
    # long_seqs_exact = LCS.exact_method(dataset.sequences)
    # print(long_seqs_exact)
    # print(time.process_time() - start_time)

    # start_time = time.process_time()
    # long_seqs_optimal = LCS.genetic_algorithm(chromosomes=dataset.sequences, population_size=1000, mutation_rate=0.10, max_gens=100, selection_method=SelectionMethod.TOURNAMENT)
    # print(long_seqs_optimal)
    # print(time.process_time() - start_time)


if __name__ == '__main__':
    setup()
    main()
