#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1],
    4: [1, 5, 7, 8],
    5: [4, 6],
    6: [5, 7],
    7: [4, 6],
    8: [4],
}


def n_swaps(cnot):
    """Count the minimum number of swaps needed to create the equivalent CNOT.

    Args:
        - cnot (qml.Operation): A CNOT gate that needs to be implemented on the hardware
        You can find out the wires on which an operator works by asking for the 'wires' attribute: 'cnot.wires'

    Returns:
        - (int): minimum number of swaps
    """

    # QHACK #
    def check_if_adjacent(node1, node2, graph):
        if node1 in graph[node2]:
            return True

    def return_path_length(node1, node2, graph, length, visited):
        if check_if_adjacent(node1, node2, graph):
            return length
        else:
            queue = []                # Local queue to visit from this node
            visited.append(node1)
            #print("Node: {}, Visited: {}".format(node1, visited))
            length += 1
            
            for node in graph[node1]:
                if node not in visited:
                    queue.append(node)
                    
            #print("From node {}, queue is {}".format(node1, queue))        
            for node in queue:
                #print("From node {} going to {} \n".format(node1, node)) 
                queue.remove(node)
                result = return_path_length(node, node2, graph, length, visited)
                if result:
                    return result

    visited = []
    length = 1                
    return (return_path_length(*list(cnot.wires), graph, length, visited)-1)*2

    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    output = n_swaps(qml.CNOT(wires=[int(i) for i in inputs]))
    print(f"{output}")
