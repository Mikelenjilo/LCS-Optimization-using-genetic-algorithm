from random import randint, random
from genetic_algorithm.models.chromosome_model import Chromosome
from genetic_algorithm.models.selection_method_model import SelectionMethod


def generate_first_gen(population_size: int, motif: str) -> list[Chromosome]:
    first_gen: list[Chromosome] = []

    for _ in range(population_size):
        seq: Chromosome = Chromosome(motif=motif, array=[0] * len(motif))
        for i in range(len(motif)):
            seq.array[i] = randint(0, 1)
        seq.get_seq_from_array()
        first_gen.append(seq)

    return first_gen


def evaluate_gen(min_seq: str, first_gen: list[Chromosome], sequences: list[str]):
    for seq in first_gen:
        l: int = 0
        for i in range(len(seq.array)):
            if seq.array[i] == 1:
                l += 1

        m: int = calculate_m(seq.sequence, sequences)
        v: int = l + 30 * m
        K: int = len(sequences)

        if l == len(min_seq):
            v += 50
        if m == K:
            v *= 3000
        else:
            v = -1000 * v * (K - m)

        seq.fitness = v


def calculate_m(sub_seq: str, sequences: list[str]) -> int:
    counter: int = 0
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
            counter += 1

    return counter


def generate_gens(mutation_rate: float, first_gen: list[Chromosome], selection_method: SelectionMethod,
                  max_gens: int, chromosomes: list[str]) -> Chromosome:
    best_solution: Chromosome | None = first_gen[0]
    for a in first_gen:
        if a.fitness > best_solution.fitness:
            best_solution = a

    if selection_method == SelectionMethod.TOURNAMENT:
        previous_gen: list[Chromosome] = list(first_gen)
        new_gen: list[Chromosome] = []
        for _ in range(max_gens):
            while len(new_gen) != len(previous_gen):
                parent_1: Chromosome = tournament(previous_gen)
                parent_2: Chromosome = tournament(previous_gen)

                child_1, child_2 = crossover(parent_1, parent_2)
                mutation(mutation_rate, child_1)
                mutation(mutation_rate, child_2)

                new_gen.append(child_1)
                new_gen.append(child_2)
            previous_gen = list(new_gen)
            evaluate_gen(new_gen[0].motif, new_gen, chromosomes)
            best_solution: Chromosome = new_gen[0]
            for a in new_gen:
                if a.fitness > best_solution.fitness:
                    best_solution = a

        return best_solution

    else:
        return NotImplemented


def tournament(generation: list[Chromosome]) -> Chromosome:
    chromosome_1: Chromosome = generation[randint(0, len(generation) - 1)]
    chromosome_2: Chromosome = generation[randint(0, len(generation) - 1)]
    if chromosome_1.fitness >= chromosome_2.fitness:
        return chromosome_1
    else:
        return chromosome_2


def crossover(parent_1: Chromosome, parent_2: Chromosome) -> tuple[Chromosome, Chromosome]:
    i: int = randint(1, min(len(parent_1.array), len(parent_2.array)))
    array_1: list[int] = parent_1.array[:i] + parent_2.array[i:]
    array_2: list[int] = parent_2.array[:i] + parent_1.array[i:]

    child_1: Chromosome = Chromosome(motif=parent_1.motif, array=array_1)
    child_2: Chromosome = Chromosome(motif=parent_1.motif, array=array_2)

    child_1.get_seq_from_array()
    child_2.get_seq_from_array()

    return child_1, child_2


def mutation(mutation_rate: float, chromosome: Chromosome):
    for i in range(len(chromosome.array)):
        a: float = random()
        if a <= mutation_rate:
            chromosome.array[i] = 0 if chromosome.array[i] == 1 else 1
    chromosome.get_seq_from_array()
