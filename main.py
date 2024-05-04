from setup import setup
from lcs import LCS
from dataset_generation.helper_functions import generate_dataset
from dataset_generation.models.dataset_model import Dataset
from genetic_algorithm.models.selection_method_model import SelectionMethod
import time


def main():
    dataset: Dataset = generate_dataset(alphabet=['A', 'B', 'C'], nb_seqs=50, seq_length=15)

    start_time = time.process_time()
    long_seqs_exact = LCS.exact_method(dataset.sequences)
    print(long_seqs_exact)
    print(time.process_time() - start_time)

    start_time = time.process_time()
    long_seqs_optimal = LCS.genetic_algorithm(chromosomes=dataset.sequences, population_size=500, mutation_rate=0.10, max_gens=100, selection_method=SelectionMethod.TOURNAMENT)
    print(long_seqs_optimal)
    print(time.process_time() - start_time)



if __name__ == '__main__':
    setup()
    main()
