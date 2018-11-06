#!/usr/bin/env python3
# Niki Thomas(nikthoma)

"""
Longest Path in a DAG Problem
Find a longest path between two nodes in an edge-weighted DAG.

Given: An integer representing the source node of a graph,
followed by an integer representing the sink node of the graph, followed by an edge-weighted graph.
The graph is represented by a modified adjacency list in which the notation "0->1:7" indicates that
an edge connects node 0 to node 1 with weight 7.

Return: The length of a longest path in the graph, followed by a longest path.
(If multiple longest paths exist, you may return any one.)

"""

import sys, re, ast

from collections import defaultdict


class Graph:
    """
    This class represents a directed graph using adjacency list representation.
    cr: GeeksforGeeks
    """

    def __init__(self, vertices):

        self.V = vertices  # number of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    def addedge(self, u, v):
        """
        Function to add edges to graph.
        """
        self.graph[u].append(v)
        print(self.graph)

    def outpath(self, u, d, visited, path):
        """
        Recursive topological sort function.
        """

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path, file=open('paths.txt', 'a+'))

        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                print(i)
                if visited[i] == False:
                    self.outpath(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    def genpath(self, s, d):
        """
        Prints all paths from source to sink node.
        """

        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.outpath(s, d, visited, path)


graph = []  # initialize graph list


def topsort():
    """
    Passes data to Graph class to create graph and do topological sort.
    :return: All possible paths from source node to sink node.
    """

    data = []  # raw data

    for line in sys.stdin.readlines():
        data.append(line.strip())

    sourcenode = int(data[0])
    sinknode = int(data[1])

    # delete the source and sink nodes from the data list
    del data[0]
    del data[0]

    # generate graph, list of edges, and list of destination nodes
    edges = []
    v = []  # destination nodes
    for i in range(len(data)):
        cleandata = re.findall(r"\d+", data[i])
        graph.append([int(cleandata[0]), [int(cleandata[1]), int(cleandata[2])]])
        edges.append([int(cleandata[0]), int(cleandata[1])])
        v.append(int(cleandata[1]))

    print(*graph, sep="\n")

    # create a list of all nodes to get vertices
    nodes = []
    nodes.append(sourcenode)
    nodes.append(sinknode)

    for item in v:
        if item not in nodes:
            nodes.append(item)

    vertices = len(nodes)

    # Generate graph and do topological sort
    g = Graph(vertices)

    for x in range(len(edges)):
        g.addedge(edges[x][0], edges[x][1])

    g.genpath(sourcenode, sinknode)

    return graph


def findlongestpath(graph):
    """
    Calculates score by adding weights of each path, then prints longest path.
    :return: longest path
    """

    # import paths and convert to usable lists
    with open('paths.txt', 'r') as f:
        paths = [line.strip() for line in f]

    for i in range(len(paths)):
        paths[i] = ast.literal_eval(paths[i])  # cr: Stack Overflow

    # get the length of all of the paths
    lengths = {}
    for path in range(len(paths)):
        lengths.update({len(paths[path]): paths[path]})

    # find the longest path
    longestpath = lengths.get(max(k for k, v in lengths.items() if v != 0))

    # add weights of longest path and score it
    score = 0
    for i in range(len(longestpath)):
        # for each node in the given path
        for x in range(len(graph)):
            # for each step in the graph
            if longestpath[i] == graph[x][0] and longestpath[i+1] == graph[x][1][0]:
                # if the current node = initial node and current node + 1 = the destination node
                score += graph[x][1][1]
                # add the weight of that path to the score

    print(score)
    print(*longestpath, sep="->")


if __name__ == "__main__":

    topsort()
    findlongestpath(graph)
