# 2018-2019 Programação 2 LTI
# Grupo 69
# 49187 Sofia Torres
# 50383 João Paiva

def searchII(graph, start, end):
    """
    Returns the fastest path from start node to end node by a DFS
    Requires: graph a DigraphII object, start and end are nodesII objects
    Ensures: shortest path from start to end in graph
    """
    return DFSII(graph, start, end, [], 0, None)

def DFSII(graph, start, end, path, time, fastest):
    """
    Requires:
    graph a Digraph;
    start and end nodes;
    path as list of nodes;
    time as float
    Ensures:
    the fastest time from start node to end node
    """
    path = path + [start]

    if len(path) > 1:
        time = time + graph.calculatetime(path[-2], path[-1])

    if start == end:
        return time
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if fastest == None or time < fastest:
                newTime = DFSII(graph, node, end, path, time, fastest)
                if fastest == None:
                    fastest = newTime
                elif newTime < fastest:
                    fastest = newTime
    return fastest
