from random import randint, choices
from dataset_generation.models.dataset_model import Dataset


def generate_dataset(alphabet: list[str], nb_seqs: int, seq_length: int, var_length: bool = False) -> Dataset:
    sequences: list[str] = []
    a: int = seq_length

    for _ in range(nb_seqs):
        if var_length:
            a = randint(1, seq_length)

        sequences.append(''.join(choices(alphabet, k=a)))

    return Dataset(
        alphabet=alphabet,
        nb_seqs=nb_seqs,
        seq_length=seq_length,
        sequences=sequences,
        var_length=var_length
    )
