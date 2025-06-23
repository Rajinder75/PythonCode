# the below dict contains the nodes and their connection to different nodes + their distances
my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}


#the parameters are the graph and node where the algorithm will start.
#target is the additional argument to return only the path between two nodes.
def shortest_path(graph, start, target=""):
    # the below list construct stores the nodes as a form of a list
    unvisited = list(graph)

    # dict comprehension is used below to store the distances between the starting node and all other nodes.
    # see if the node in the graph is same as starting node, the distance is set to ZERO (A to A is zero)
    # But as the distance between others is unknown infinite value is assigneed for the moment
    distances = {node: 0 if node == start else float('inf') for node in  graph}
    

    # in paths (to keep track of paths between starting node and all other nodes), 
    # nodes form the graph are stored with emtpy lists using dictionary comprehension
    paths = {node: [] for node in graph}
    
    # As the algorithm starts the assessment from from starting node, 
    # adding the node to the path dictionary:
    paths[start].append(start) # it adds the starting node in the list ofthe starting node key
    

    # Your function is going to explore all the nodes connected to the starting node. 
    # It will calculate the shortest paths for all of them. 
    # Then, it will remove the starting node from the unvisited nodes.
    # Next, the closest neighbor node will be visited and the process will be repeated until
    #  all the nodes are visited.

    # this while loops runs when the unvisited is not empty [has True boolean value]
    while unvisited:
        #defining the current node to visit, min returns the smallest item from the iterable
        #passing a funciton as the second argument, you can modify how min functions compares the list items
        # the below line of code selects the node with the smallest distance from the starting node
        current = min(unvisited, key=distances.get)
        print("current", current)

        #for loop to iterate over the elements of the tuples
        for node, distance in graph[current]:
            print("node and distance", node, distance)
            # checks if the distance of the neighbor node (the second item in the processed tuple) 
            # plus the distance of current is less than the currently known distance 
            # of the neighbor node (the first item in the processed tuple).
            print("distance", distance,"distances[current]",distances[current],"distances[node]", distances[node])
            if distance + distances[current] < distances[node]:
                #when the above condition gets true, it means a shorter distance has been found
                distances[node] = distance + distances[current]

                #you also need to keep track of the paths to that node
                #If the distance for the node in the processed tuple has been updated, 
                #the last item in its path is the node itself.

                #to check if the last item in paths is equal to the node itself.
                #it also checks if it empty or not (otherwise it might throw an error if it is empty)
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:] #creating a copy by slicing to prevent copying of changes
                else:
                    #adding the current node path to the neighbor node path.
                    paths[node].extend(paths[current])
                #appending neighbour node to its path
                paths[node].append(node)
        #terminating the while loop by removing the current node from the unvisited list
        unvisited.remove(current)

    #assigns [targets] if target is truthy othwewise graph
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        #to skip the printing of the distance between the starting node and starting node (ZERO)
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    return distances, paths
    #print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')

#if you add the third argument, then only the path to that node from the starting node + distance 
#will be displayed
shortest_path(my_graph, 'A')


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
