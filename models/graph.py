from dataclasses import dataclass, field
from models.node import Node
from models.edge import Edge


@dataclass
class Graph:
    nodes: dict = field(default_factory=dict) # creates own dict
    edges: dict = field(default_factory=dict)

    def add_node(self, node):
        self.nodes[node.id] = node

    def add_edge(self, edge):
        self.edges[edge.id] = edge

    def get_all_nodes(self):
        return self.nodes
    
    def get_all_edges(self):
        return self.edges