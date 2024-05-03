from exact_method.helper_functions import get_small_seq, get_long_seq, get_seqs_array, get_seq_str, evaluate_seqs

class LCS:
    @staticmethod
    def longest_common_subsequence(sequences: list[str]) -> list[str]:
        min_seq: str = get_small_seq(sequences)
        seqs_array: list[list[int]] = get_seqs_array(min_seq)
        seq_str: list[str] = get_seq_str(min_seq, seqs_array)
        sequences.remove(min_seq)

        valid_seqs: list[str] = []
        for sub_seq in seq_str:
            a: str = evaluate_seqs(sub_seq, sequences)
            if a and a not in valid_seqs:
                valid_seqs.append(a)

        if valid_seqs:
            return get_long_seq(valid_seqs)
        else:
            return []

