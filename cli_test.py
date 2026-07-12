import sys
from models.node import Node
from models.edge import Edge
from models.graph import Graph
from uuid import uuid4

if __name__ == "__main__":

    graph = Graph()
    command = sys.argv[1]

    if command == "add-node":
        label = sys.argv[2]       
        node = Node(              
            id=str(uuid4()),
            label=label,           
            x=0.0,
            y=0.0
        )
        graph.add_node(node)
        print(f"Node created: {label}")
    elif command == "list-nodes":
        nodes = graph.get_all_nodes()
        for node_id, node in nodes.items():
            print(f"{node.label} (id: {node.id})")

    else:
        print(f"Unknown command: {command}")