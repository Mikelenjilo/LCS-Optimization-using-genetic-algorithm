class Chromosome:
    def __init__(self, motif: str, array: list[int], fitness: int | None = None, sequence: str | None = None):
        self.array = array
        self.fitness = fitness
        self.sequence = sequence
        self.motif = motif

    def get_str_from_array(self):
        a: str = ''

        for i in range(len(self.array)):
            if self.array[i] == 1:
                a += self.motif[i]

        self.sequence = a

    def __str__(self):
        return "Sequence(motif: {}, array: {}, sequence: {}, fitness: {})".format(self.motif, self.array, self.sequence, self.fitness)
