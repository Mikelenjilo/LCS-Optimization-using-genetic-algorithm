from setup import setup
from exact_method.lcs import LCS


def main():
    sequences: list[str] = ['MASSI', 'MASSII', 'MASSI', 'KDJFKD', 'DKJFDKJ']
    long_seqs = LCS.longest_common_subsequence(sequences)

    print(long_seqs)

if __name__ == '__main__':
    setup()
    main()
