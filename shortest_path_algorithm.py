# the below dict contains the nodes and their connection to different nodes + their distances
my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

#the parameters are the graph and node where the algorithm will start.
def shortest_path(graph, start):
    # the below list construct stores the nodes as a form of a list
    unvisited = list(graph)

    # dict comprehension is used below to store the distances between the starting node and all other nodes.
    # see if the node in the graph is same as starting node, the distance is set to ZERO (A to A is zero)
    # But as the distance between others is unknown infinite value is assigneed for the moment
    distances = {node: 0 if node == start else float('inf') for node in  graph}

    

    # in paths (to keep track of paths between starting node and all other nodes), nodes form the graph are stored with emtpy lists using dictionary comprehension
    paths = {node: [] for node in graph}









































"""
def shortest_path(graph, start):
    --- the below list is for storing the unvisited nodes, the visited nodes will be removed
    unvisited = []
    --- distances dictionary store the distances between the starting node and all nodes in the graph.
    distances = {}
    for node in graph:
    --- iterates through the dictionary and appends the nodes into the list
        unvisited.append(node)
    --- if the node is same as the starting node, the distance is zero (distance from A to A is ZERO)
        if node == start:
            distances[node] = 0
    --- otherwise the distance is set to inf
        else:
            distances[node] = float('inf')
    print(f'Unvisited: {unvisited}\nDistances: {distances}')
    
shortest_path(my_graph, 'A')
"""
