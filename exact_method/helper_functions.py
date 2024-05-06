from itertools import product


def get_small_chrom(seqs: list[str]) -> str:
    min_len: int = len(seqs[0])
    min_seq: str = seqs[0]
    for seq in seqs:
        if len(seq) < min_len:
            min_seq = seq
            min_len = len(seq)

    return min_seq


def get_long_seqs(seqs: list[str]) -> list[str]:
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

        if motif and motif not in seqs:
            seqs.append(motif)

    return seqs


def compare_seqs(sub_seq: str, sequences: list[str]) -> str:
    z: int = 0
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
            z += 1

    if z == len(sequences):
        return sub_seq


def evaluate_seq(l: int, m: int, seq_length: int):
    v: int = l + 30 * m

    if l == seq_length:
        v += 50

    v *= 3000

    return v
