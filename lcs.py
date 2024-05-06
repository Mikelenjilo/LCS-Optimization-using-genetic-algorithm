from exact_method.helper_functions import get_small_chrom, get_long_seqs, get_seqs_array, get_seq_str, compare_seqs, evaluate_seq
from genetic_algorithm.models.selection_method_model import SelectionMethod
from genetic_algorithm.helper_functions import generate_first_gen, evaluate_gen, generate_gens
from genetic_algorithm.models.chromosome_model import Chromosome


class LCS:
    @staticmethod
    def exact_method(sequences: list[str]) -> list[tuple[str, int]]:
        min_seq: str = get_small_chrom(sequences)
        seqs_array: list[list[int]] = get_seqs_array(min_seq)
        seqs_str: list[str] = get_seq_str(min_seq, seqs_array)
        sequences.remove(min_seq)

        valid_seqs: list[str] = []
        for sub_seq in seqs_str:
            a: str = compare_seqs(sub_seq, sequences)
            if a and a not in valid_seqs:
                valid_seqs.append(a)

        if valid_seqs:
            lcs: list[tuple[str, int]] = []
            temp = get_long_seqs(valid_seqs)
            for a in temp:
                lcs.append((a, evaluate_seq(l=len(a), m=len(sequences), seq_length=len(min_seq))))

            return lcs
        else:
            return []

    @staticmethod
    def genetic_algorithm(chromosomes: list[str], population_size: int, mutation_rate: float, max_gens: int,
                          selection_method: SelectionMethod) -> tuple[str, int]:
        min_chrom: str = get_small_chrom(chromosomes)
        first_gen: list[Chromosome] = generate_first_gen(population_size, min_chrom)
        evaluate_gen(min_chrom, first_gen, chromosomes)
        best_solution: Chromosome = generate_gens(mutation_rate=mutation_rate, first_gen=first_gen, selection_method=selection_method, max_gens=max_gens, chromosomes=chromosomes)

        return best_solution.sequence, best_solution.fitness
