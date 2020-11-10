################################################################################
# # Starter code for Problem 1
# Author: praty@stanford.edu
# Last Updated: Sep 28, 2017
################################################################################

import snap
import numpy as np
import matplotlib.pyplot as plt

# Setup
erdosRenyi = None
smallWorld = None
collabNet = None


# Problem 1.1
def genErdosRenyi(N=5242, E=14484):
    """
    :param - N: number of nodes
    :param - E: number of edges

    return type: snap.PUNGraph
    return: Erdos-Renyi graph with N nodes and E edges
    """
    ############################################################################
    # TODO: Your code here!
    Graph = snap.GenRndGnm(snap.PNGraph,N,E)

    ############################################################################
    return Graph


def genCircle(N=5242):
    """
    :param - N: number of nodes

    return type: snap.PUNGraph
    return: Circle graph with N nodes and N edges. Imagine the nodes form a
        circle and each node is connected to its two direct neighbors.
    """
    ############################################################################
    # TODO: Your code here!
    Graph = None
    ############################################################################
    return Graph


def connectNbrOfNbr(Graph, N=5242):
    """
    :param - Graph: snap.PUNGraph object representing a circle graph on N nodes
    :param - N: number of nodes

    return type: snap.PUNGraph
    return: Graph object with additional N edges added by connecting each node
        to the neighbors of its neighbors
    """
    ############################################################################
    # TODO: Your code here!

    ############################################################################
    return Graph


def connectRandomNodes(Graph, M=4000):
    """
    :param - Graph: snap.PUNGraph object representing an undirected graph
    :param - M: number of edges to be added

    return type: snap.PUNGraph
    return: Graph object with additional M edges added by connecting M randomly
        selected pairs of nodes not already connected.
    """
    ############################################################################
    # TODO: Your code here!

    ############################################################################
    return Graph


def genSmallWorld(N=5242, E=14484):
    """
    :param - N: number of nodes
    :param - E: number of edges

    return type: snap.PUNGraph
    return: Small-World graph with N nodes and E edges
    """
    Graph = genCircle(N)
    Graph = connectNbrOfNbr(Graph, N)
    Graph = connectRandomNodes(Graph, 4000)
    return Graph


def loadCollabNet(path):
    """
    :param - path: path to edge list file

    return type: snap.PUNGraph
    return: Graph loaded from edge list at `path and self edges removed

    Do not forget to remove the self edges!
    """
    ############################################################################
    # TODO: Your code here!
    Graph = None

    ############################################################################
    return Graph


def getDataPointsToPlot(Graph):
    """
    :param - Graph: snap.PUNGraph object representing an undirected graph
    
    return values:
    X: list of degrees
    Y: list of frequencies: Y[i] = fraction of nodes with degree X[i]
    """
    ############################################################################
    # TODO: Your code here!
    X, Y = [], []

    ############################################################################
    return X, Y


def Q1_1():
    """
    Code for HW1 Q1.1
    """
    global erdosRenyi, smallWorld, collabNet
    erdosRenyi = genErdosRenyi(5242, 14484)
    smallWorld = genSmallWorld(5242, 14484)
    collabNet = loadCollabNet("ca-GrQc.txt")

    x_erdosRenyi, y_erdosRenyi = getDataPointsToPlot(erdosRenyi)
    plt.loglog(x_erdosRenyi, y_erdosRenyi, color = 'y', label = 'Erdos Renyi Network')

    x_smallWorld, y_smallWorld = getDataPointsToPlot(smallWorld)
    plt.loglog(x_smallWorld, y_smallWorld, linestyle = 'dashed', color = 'r', label = 'Small World Network')

    x_collabNet, y_collabNet = getDataPointsToPlot(collabNet)
    plt.loglog(x_collabNet, y_collabNet, linestyle = 'dotted', color = 'b', label = 'Collaboration Network')

    plt.xlabel('Node Degree (log)')
    plt.ylabel('Proportion of Nodes with a Given Degree (log)')
    plt.title('Degree Distribution of Erdos Renyi, Small World, and Collaboration Networks')
    plt.legend()
    plt.show()


# Execute code for Q1.1
Q1_1()

# Problem 1.2

# Find max degree of all 3 graphs for plotting (add 2 for padding)
maxdeg = max([erdosRenyi.GetNI((snap.GetMxDegNId(erdosRenyi))).GetDeg(),
                smallWorld.GetNI((snap.GetMxDegNId(smallWorld))).GetDeg(),
                collabNet.GetNI((snap.GetMxDegNId(collabNet))).GetDeg()]) + 2

# Erdos Renyi
def calcQk(Graph, maxDeg=maxdeg):
    """
    :param Graph - snap.PUNGraph object representing an undirected graph
    :param maxDeg - maximum degree(+1) for which q_k needs to be calculated
    
    return type: np.array
    return: array q_k of dimension maxDeg representing the excess degree
        distribution  
    """
    ############################################################################
    # TODO: Your code here!
    q_k = np.zeros(maxDeg)

    ############################################################################
    return q_k


def calcExpectedDegree(Graph):
    """
    :param Graph - snap.PUNGraph object representing an undirected graph

    return type: float
    return: expected degree of Graph
    """
    ############################################################################
    # TODO: Your code here!
    ed = 0.0

    ############################################################################
    return ed


def calcExpectedExcessDegree(Graph, qk):
    """
    :param Graph - snap.PUNGraph object representing an undirected graph
    :param qk - np.array of dimension maxdeg representing excess degree
        distribution of `Graph

    return type: float
    return: expected excess degree of `Graph
    """
    ############################################################################
    # TODO: Your code here!
    eed = 0.0

    ############################################################################
    return eed


def Q1_2_a():
    """
    Code for Q1.2a
    """
    qk_erdosRenyi = calcQk(erdosRenyi, maxdeg)
    qk_smallWorld = calcQk(smallWorld, maxdeg)
    qk_collabNet = calcQk(collabNet, maxdeg)

    plt.loglog(range(maxdeg), qk_erdosRenyi, color = 'y', label = 'Erdos Renyi Network')
    plt.loglog(range(maxdeg), qk_smallWorld, linestyle = 'dashed', color = 'r', label = 'Small World Network')
    plt.loglog(range(maxdeg), qk_collabNet, linestyle = 'dotted', color = 'b', label = 'Collaboration Network')

    plt.xlabel('k Degree')
    plt.ylabel('Excess Degree Distribution')
    plt.title('Excess Degree Distribution of Erdos Renyi, Small World, and Collaboration Networks')
    plt.legend()
    plt.show()

    # Calculate Expected Degree
    ed_erdosRenyi = calcExpectedDegree(erdosRenyi)
    ed_smallWorld = calcExpectedDegree(smallWorld)
    ed_collabNet = calcExpectedDegree(collabNet)
    print 'Expected Degree for Erdos Renyi: %f' % ed_erdosRenyi
    print 'Expected Degree for Small World: %f' % ed_smallWorld
    print 'Expected Degree for Collaboration Network: %f' % ed_collabNet

    # Calculate Expected Excess Degree
    eed_erdosRenyi = calcExpectedExcessDegree(erdosRenyi, qk_erdosRenyi)
    eed_smallWorld = calcExpectedExcessDegree(smallWorld, qk_smallWorld)
    eed_collabNet = calcExpectedExcessDegree(collabNet, qk_collabNet)
    print 'Expected Excess Degree for Erdos Renyi: %f' % (eed_erdosRenyi)
    print 'Expected Excess Degree for Small World: %f' % (eed_smallWorld)
    print 'Expected Excess Degree for Collaboration Network: %f' % (eed_collabNet)


# Execute code for Q1.2a
Q1_2_a()


# Problem 1.3 - Clustering Coefficient

def calcClusteringCoefficient(Graph):
    """
    :param - Graph: snap.PUNGraph object representing an undirected graph

    return type: float
    returns: clustering coeffient of `Graph 
    """    
    ############################################################################
    # TODO: Your code here!
    C = 0.0

    ############################################################################
    return C

def Q1_3():
    """
    Code for Q1.3
    """
    C_erdosRenyi = calcClusteringCoefficient(erdosRenyi)
    C_smallWorld = calcClusteringCoefficient(smallWorld)
    C_collabNet = calcClusteringCoefficient(collabNet)
    
    print('Clustering Coefficient for Erdos Renyi Network: %f' % C_erdosRenyi)
    print('Clustering Coefficient for Small World Network: %f' % C_smallWorld)
    print('Clustering Coefficient for Collaboration Network: %f' % C_collabNet)


# Execute code for Q1.3
Q1_3()

