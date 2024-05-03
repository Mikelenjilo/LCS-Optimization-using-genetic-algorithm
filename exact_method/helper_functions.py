from itertools import product


def get_small_seq(seqs: list[str]) -> str:
    min_len: int = len(seqs[0])
    min_seq: str = seqs[0]
    for seq in seqs:
        if len(seq) < min_len:
            min_seq = seq
            min_len = len(seq)

    return min_seq


def get_long_seq(seqs: list[str]) -> list[str]:
    max_len: int = len(seqs[0])
    max_seqs: list[str] = []
    for seq in seqs:
        if len(seq) > max_len:
            max_len = len(seq)

    for seq in seqs:
        if len(seq) == max_len:
            max_seqs.append(seq)

    return max_seqs


def get_seqs_array(seq: str):
    array: list[list[int]] = []
    for bits in product([0, 1], repeat=len(seq)):
        array.append(list(bits))

    return array


def get_seq_str(seq: str, seq_array: list[list[int]]) -> list[str]:
    seqs: list[str] = []
    for array in seq_array:
        motif: str = ''
        for i in range(len(array)):
            if array[i] == 1:
                motif = motif + seq[i]

        if motif:
            seqs.append(motif)

    return seqs


def evaluate_seqs(sub_seq: str, sequences: list[str]) -> str:
    k_array: list[int] = []
    for seq in sequences:
        i: int = 0
        j: int = 0
        k: int = 0

        while i < len(sub_seq) and j < len(seq):
            if sub_seq[i] == seq[j]:
                i += 1
                j += 1
                k += 1
            else:
                j += 1

        if k == len(sub_seq):
            k_array.append(k)

    if len(k_array) == len(sequences):
        return sub_seq
    # for seq in sequences:
    # for node in nodes:
    #     i: int = 0
    #     j: int = 0
    #     k: int = 0
    #     score: int = 0
    #     sub_seq: str = node.sub_sequence
    #
    #     while i < len(sub_seq) and j < len(seq):
    #         if sub_seq[i] == seq[j]:
    #             i += 1
    #             j += 1
    #             k += 1
    #         else:
    #             j += 1
    #
    #     if k == len(sub_seq):
    #         score += 1
    #         node.score = score
