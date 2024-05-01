from setup import setup
from exact_method.lcs import LCS


def main():
    motif: str = 'MASSI'
    sequences: list[str] = ['MADJID', 'MALIKA', 'KOCEILA']
    long_seqs = LCS.longest_common_subsequence(motif, sequences)
    print(long_seqs)


if __name__ == '__main__':
    setup()
    main()
