from exact_method.models.graph_model import Graph
from exact_method.models.node_model import Node
from collections import deque




class BFS:
    @staticmethod
    def create_graph(motif: str):
        all_sub_seqs: list[list] = get_all_sub_seqs(motif)
        print(all_sub_seqs)




def get_all_sub_seqs(root: str) -> list[list]:
    ouvert: list[str] = [root]
    all_sub_seqs: list[list] = []

    while ouvert:
        n = ouvert.pop(0)
        if len(n) == 1:
            break
        else:
            sub_seqs: list[str] = get_sub_seqs(n, all_sub_seqs)
            ouvert = ouvert + sub_seqs
            sub_seqs.insert(0, n)
            all_sub_seqs.append(sub_seqs)

    return all_sub_seqs


def get_sub_seqs(motif: str, seqs: list[list]) -> list[str]:
    sub_seqs: list[str] = []

    for i in range(len(motif)):
        word: str = motif[:i] + motif[i+1:]
        sub_seqs.append(word)

    return sub_seqs

