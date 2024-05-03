from exact_method.helper_functions import get_small_seq, get_seqs_array, get_seq_str

class LCS:
    @staticmethod
    def longest_common_subsequence(sequences: list[str]) -> list[str]:
        min_seq: str = get_small_seq(sequences)
        seqs_array: list[list[int]] = get_seqs_array(min_seq)
        seq_str: list[str] = get_seq_str(min_seq, seqs_array)

        sequences.remove(min_seq)






