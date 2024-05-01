from exact_method.models.node_model import Node
from exact_method.models.graph_model import Graph


def create_graph(motif: str) -> Graph:
    all_sub_seqs: list[list] = get_all_sub_seqs(motif)
    nodes: list[Node] = get_all_nodes(all_sub_seqs)
    graph: Graph = Graph(size=len(nodes))
    graph.add_nodes(nodes)
    graph.add_edges(nodes, all_sub_seqs)
    return graph


def get_all_sub_seqs(root: str) -> list[list]:
    ouvert: list[str] = [root]
    all_sub_seqs: list[list] = []

    while ouvert:
        n = ouvert.pop(0)
        if len(n) == 1:
            break
        else:
            sub_seqs: list[str] = get_sub_seqs(n, all_sub_seqs)
            ouvert = ouvert + sub_seqs[1:]
            all_sub_seqs.append(sub_seqs)

    return all_sub_seqs


def get_sub_seqs(motif: str, seqs: list[list[str]]) -> list[str]:
    sub_seqs: list[str] = []
    remove_words: list[str] = []

    for i in range(len(motif)):
        word: str = motif[:i] + motif[i + 1:]
        if word not in sub_seqs:
            sub_seqs.append(word)

    sub_seqs.insert(0, motif)
    for i in range(1, len(sub_seqs)):
        word: str = sub_seqs[i]
        for j in range(1, len(seqs)):
            for z in range(1, len(seqs[j])):
                if word == seqs[j][z]:
                    remove_words.append(word)
                    break

    for word in remove_words:
        sub_seqs.remove(word)

    return sub_seqs


def get_all_nodes(sub_seqs: list[list[str]]) -> list[Node]:
    nodes: list[Node] = []

    for i in range(len(sub_seqs)):
        for j in range(len(sub_seqs[i])):
            node: Node = Node(sub_sequence=sub_seqs[i][j], score=0)
            if node not in nodes:
                nodes.append(node)

    return nodes


def evaluate_nodes(nodes: list[Node], sequences: list[str]):
    for seq in sequences:
        for node in nodes:
            i: int = 0
            j: int = 0
            k: int = 0
            score: int = 0
            sub_seq: str = node.sub_sequence

            while i < len(sub_seq) and j < len(seq):
                if sub_seq[i] == seq[j]:
                    i += 1
                    j += 1
                    k += 1
                else:
                    j += 1

            if k == len(sub_seq):
                score += 1
                node.score = score


def get_longest_prefix(nodes: list[Node]) -> list[str]:
    long_seqs: list[str] = []
    long_seqs_nodes: list[Node] = []
    for node in nodes:
        if node.score != 0:
            long_seqs_nodes.append(node)

    long_seq_len: int = len(long_seqs_nodes[0].sub_sequence)
    for node in long_seqs_nodes:
        if len(node.sub_sequence) == long_seq_len:
            long_seqs.append(node.sub_sequence)

    return long_seqs

