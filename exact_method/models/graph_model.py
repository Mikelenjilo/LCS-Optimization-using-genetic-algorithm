import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

from exact_method.models.node_model import Node


class Graph:
    def __init__(self, size: int):
        self.matrix: list[list[int]] = [[0] * size for _ in range(size)]
        self.nodes: list[Node] = []

    def add_node(self, node: Node):
        node.id = len(self.nodes)
        self.nodes.append(node)

    def add_nodes(self, nodes: list[Node]):
        for node in nodes:
            node.id = len(self.nodes)
            self.nodes.append(node)

    def add_edge(self, src: Node, dst: Node):
        self.matrix[src.id][dst.id] = 1

    def draw(self):
        g: nx.Graph = nx.from_numpy_array(np.array(self.matrix))
        pos = graphviz_layout(g, prog='dot')

        labels = {}
        for node in self.nodes:
            labels[node.id] = node.sub_sequence

        nx.draw_networkx(g, pos, with_labels=True, labels=labels, node_size=2000)
        plt.show()
