from exact_method.models.graph_model import Graph
from exact_method.helper_functions import create_graph, evaluate_nodes, get_longest_prefix

class LCS:
    @staticmethod
    def longest_common_subsequence(motif: str, sequences: list[str]) -> list[str]:
        graph: Graph = create_graph(motif)
        evaluate_nodes(graph.nodes, sequences)
        return get_longest_prefix(graph.nodes)


