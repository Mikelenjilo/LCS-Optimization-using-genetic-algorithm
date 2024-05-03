from itertools import product


def get_small_seq(seqs: list[str]) -> str:
    min_len: int = len(seqs[0])
    min_seq: str = seqs[0]
    for seq in seqs:
        if len(seq) < min_len:
            min_seq = seq
            min_len = len(seq)

    return min_seq


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
