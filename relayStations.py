# 2018-2019 Programação 2 LTI
# Grupo 69
# 49187 Sofia Torres
# 50383 João Paiva

from NodeII import NodeII
from DigraphII import GraphII
from EdgeII import EdgeII
from searchII import searchII
import sys
# from time import *



def createnodes(file):
    """
    Creates nodes and registers node's connections by reading a file
    Requires: file as str (.txt) with the specifications given in the project instruction
    Ensures: nodelist as a list of nodeII objects, nodeedge as a dictionary with key equal
    to a node and it's values as a list of id's of nodesII objects.
    """

    lines = [line.rstrip('\n') for line in open(file)]
    nodelist = []
    nodeedge = {}
    for i in lines[1:]:

        a = i.replace('(', '').replace(')', '').replace(' ', '')
        tempvar = a.split(",")
        node = NodeII(tempvar[0], tempvar[1], tempvar[2], tempvar[3])
        nodeedge[node] = tempvar[4:]
        nodelist.append(node)

    return nodelist, nodeedge


def creategraph(nodelist,nodeedge):
    """
    Creates a digraph with edges only between nodesII objects of the same gen
    Requires: nodelist as list of nodes, nodeedge as a dictionary with key equal
    to a node and it's values as a list of id's of nodesII objects.
    Ensures: a digraphII object
    """
    ourgraph = GraphII()
    for node in nodelist:
        ourgraph.addNode(node)

    for src in nodeedge:
        for dest in nodeedge[src]:
            if src.connected(ourgraph.getnodebyid(dest)):
                if src in ourgraph.edges.keys():
                    edge = EdgeII(src, ourgraph.getnodebyid(dest))
                    ourgraph.addEdge(edge)

    return ourgraph


def searchwriteDFS(ourgraph, secondfile, outputFile):
    """
    Searchs and writes the results of DFS in the outputFile. Reads a file to get the
    start and end nodes.
    Requires: ourgraph as DigraphII object. secondfile as str (.txt)
    with the structure given in the project instructions. outputFile as str (.txt).
    Ensures: a output file with the results of the DFS of the secondfile.
    """

    writefile = open(outputFile, "w")

    lines = [line.rstrip('\n') for line in open(secondfile)]
    lines = [line.split(" ") for line in lines]

    for start, end in (lines):
        try:
            start = ourgraph.getnodebyname(start)
            try:
                end = ourgraph.getnodebyname(end)

                if start.disconnect97(end):
                    result = None
                else:
                    result = searchII(ourgraph, start, end)

                if result == None:
                    writefile.write("{} and {} do not communicate".format(start, end) + "\n")
                else:
                    writefile.write(str(result) + "\n")

            except KeyError:
                writefile.write("{} out of network \n".format(end))

        except KeyError:
            writefile.write("{} out of network \n".format(start))

    writefile.close()


def relayStations(firstinput,secondinput, outputFile):
    # ini = time()
    nodelist, nodeedge = createnodes(firstinput)
    ourgraph = creategraph(nodelist, nodeedge)
    searchwriteDFS(ourgraph, secondinput, outputFile)
    # print(time()-ini)


networt, src_des, outputfilename = sys.argv[1:]

relayStations(networt,src_des,outputfilename)

