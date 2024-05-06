import os


class Dataset:
    def __init__(self, alphabet: list[str], nb_seqs: int, seq_length: int, var_length: bool, sequences: list[str]):
        self.alphabet = alphabet
        self.nb_seqs = nb_seqs
        self.seq_length = seq_length
        self.var_length = var_length
        self.sequences = sequences

    def export_dataset(self):
        filename: str = "dataset_generation\datasets\{alphabet}_{nb_seqs}_{seq_length}_{var_length}.txt".format(
            alphabet=len(self.alphabet), nb_seqs=self.nb_seqs, seq_length=self.seq_length,
            var_length=self.var_length)
        headers: str = "alphabet: {alphabet}\nnb_seqs: {nb_seqs}\nseq_length: {seq_length}\nvar_length: {var_length}\n".format(alphabet=self.alphabet, nb_seqs=self.nb_seqs, seq_length=self.seq_length, var_length=self.var_length)
        start: str = ">>\n"
        end: str = "<<"

        if os.path.exists(filename):
            os.remove(filename)

        with open(filename, 'a') as f:
            f.write(headers)
            f.write(start)
            for seq in self.sequences:
                f.write(seq + '\n')
            f.write(end)

    @staticmethod
    def import_dataset(filename: str) -> "Dataset":
        filename = 'dataset_generation/datasets/' + filename
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")

        with open(filename, 'r') as f:
            lines = f.readlines()

        alphabet, nb_seqs, seq_length, var_length = None, None, None, None
        for line in lines:
            if line.startswith("alphabet: "):
                alphabet = line.split(":")[1].strip()
            elif line.startswith("nb_seqs: "):
                nb_seqs = int(line.split(": ")[1].strip())
            elif line.startswith("seq_length: "):
                seq_length = int(line.split(": ")[1].strip())
            elif line.startswith("var_length: "):
                var_length = (line.split(":")[1].strip() == "True")

        sequences = []
        start_index = lines.index(">>\n") + 1
        end_index = lines.index("<<")
        for line in lines[start_index:end_index]:
            sequences.append(line.strip())

        return Dataset(eval(alphabet), nb_seqs, seq_length, var_length, sequences)

    def __str__(self):
        return "Dataset(alphabet: {}, nb_seqs: {}, seq_length: {}, var_length: {}, sequences: {})".format(self.alphabet, self.nb_seqs, self.seq_length, self.var_length, self.sequences)