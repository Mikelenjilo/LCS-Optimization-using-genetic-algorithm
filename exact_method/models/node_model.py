class Node:
    def __init__(self, sub_sequence: str, score: int):
        self.id = None
        self.sub_sequence = sub_sequence
        self.score = score

    def __str__(self):
        return f"Node(id={self.id}, sub_sequence='{self.sub_sequence}', score={self.score})"

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented

        return self.sub_sequence == other.sub_sequence
