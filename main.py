from setup import setup
from exact_method.lcs import LCS
from dataset_generation.helper_functions import generate_dataset
from dataset_generation.models.dataset_model import Dataset
import time


def main():
    dataset: Dataset = generate_dataset(alphabet=['A', 'B', 'C', 'D', 'E' 'F'], nb_seqs=50, seq_length=17)

    start_time = time.process_time()
    long_seqs = LCS.longest_common_subsequence(dataset.sequences)
    print(long_seqs)
    print(time.process_time() - start_time)



if __name__ == '__main__':
    setup()
    main()
