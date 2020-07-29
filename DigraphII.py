# 2018-2019 Programação 2 LTI
# Grupo 69
# 49187 Sofia Torres
# 50383 João Paiva

from node import *
from EdgeII import EdgeII


class DigraphII(Digraph):

    def __init__(self):
        super().__init__()
        self.namenode = {}
        self.idnode = {}

    def addNode(self, node):
        """
        Adds a node to the graph node list. Adds the created node to the graph edge dicionary as a key (src).
        Adds the created node to two diferent dicionaries.
        In the first the key its the name and in the second the key is the ID, the value is the node object itself.
        Requires: node as an object of EdgeII.
        Ensures: A node, a graph edge dicionary, a id node dictionary and an name node dictionary
        """
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = {}
            self.namenode[node.getName()] = node
            self.idnode[node.getId()] = node

    def getnodebyname(self, name):
        """
        Requires: name as str
        Ensures: nodeII object
        """
        return self.namenode[name]

    def getnodebyid(self, id):
        """
        Requires: id as str
        Ensures: nodeII object
        """
        return self.idnode[id]

    def addEdge(self, edge):
        """
        Takes an edge and adds the dest to the graph edge dictionary with key value equal to the src
        Requires: edge is an object of class EdgeII
        Ensures: add the edge to the edges dictionary
        """
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')

        if src in self.edges.keys():
            if dest not in self.edges[src].keys():
                destdict = self.edges[src]
                destdict[dest] = edge.gettime()


    def childrenOf(self, node):
        """
        Returns all possible nodes that are attached to a given node
        """
        return self.edges[node].keys()

    def calculatetime(self,src,dest):
        """
        Requires: src and dest are nodes
        Ensures: the time of a given source
        """
        return self.edges[src][dest](src)


class GraphII(DigraphII):

    def addEdge(self, edge):
        DigraphII.addEdge(self, edge)
        rev = EdgeII(edge.getDestination(), edge.getSource())
        DigraphII.addEdge(self, rev)