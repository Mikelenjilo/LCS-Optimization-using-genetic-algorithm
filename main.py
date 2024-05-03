from setup import setup
from exact_method.lcs import LCS


def main():
    sequences: list[str] = ['MASSI', 'MADJID', 'MALIKA', 'KOCEILA']
    long_seqs = LCS.longest_common_subsequence(sequences)


if __name__ == '__main__':
    setup()
    main()
