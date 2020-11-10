# -*- coding: utf-8 -*-
#import matplotlib as plt
import random
import snap
import collections
import matplotlib.pyplot as plt

class Node:
   def __init__(self, index):
      self.index = index
      self.neighbors = []
      self.degree = 0

   def __repr__(self):
      return repr(self.index)

# Question 1 Network Characteristics

""" Erdos-Renyi Random graph (G(n, m) random network): Generate a random instance of this model 
by using n = 5242 nodes and picking m = 14484 edges at random. Write code to
construct instances of this model, i.e., do not call a SNAP function """


def er_randomGraph(n,m,p):
   num_edges = 0
   vertices = [Node(i) for i in range(n)]
   #edges = [(i,j) for i in xrange(n) for j in xrange(i) if (random.random() < p and (m-1)!=0)]
   edges = []
   for i in range(n):
       for(j) in range(n):
           if random.random() < p and num_edges<m:
               edges.append((i,j))
               num_edges+=1
   for (i,j) in edges:
      vertices[i].neighbors.append(vertices[j])
      vertices[j].neighbors.append(vertices[i])
   print("At the end of er random graph gen, we have num_edges = ",num_edges)
   return vertices

""" Small-World Random Network: Generate an instance from this model as follows: 
begin with n = 5242 nodes arranged as a ring, i.e., 
imagine the nodes form a circle and each node is connected to its two direct neighbors 
(e.g., node 399 is connected to nodes 398 and 400), giving us 5242 edges. 
Next, connect each node to the neighbors of its neighbors 
(e.g., node 399 is also connected to nodes 397 and 401). This gives us another 5242 edges. 
Finally, randomly select 4000 pairs of nodes not yet connected and add an edge between them. 
In total, this will make m = 5242 · 2 + 4000 = 14484 edges. 
Write code to construct instances of this model, i.e., do not call a SNAP function. """

def sw_randomGraph(n):
    vertices = [Node(i) for i in range(n)]
    edges = []
    num_edges = 0
    for i in range(n):
        for j in range(n):
            if (j==((i+1)%n) or j==((i-1)%n)):
                edges.append((i,j))
                num_edges+=1
                #print "Attaching edge bw i and j = ",i,j
            elif (j==((i+2)%n) or j==((i-2)%n)):
                edges.append((i,j))
                num_edges+=1
                #print "Attaching edge bw i and j = ",i,j
            else:
                pass
    #print("1st round: number_edges  = ",num_edges/2)
    count=0
    sec_round_num_edges = 0
    while count<8000:
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        if ((i,j) not in edges) and ((j,i) not in edges):
            edges.append((i,j))
            #print "Attaching edge bw i and j = ",i,j
            count = count+1
            sec_round_num_edges+=1
        else:
            pass
    #print("2nd round: number_edges = ",sec_round_num_edges/2)
    #print("Count = ",count)
    #print("final number of edges = ",len(edges)/2)
    try:
        for (i,j) in edges:
            vertices[i].neighbors.append(vertices[j])
            vertices[j].neighbors.append(vertices[i])
    except:
        pass
    return vertices

#small_world_graph = sw_randomGraph(5242)

""" Real-World Collaboration Network: Download this undirected network from homework folder 
ca-GrQc.txt.gz. Nodes in this network represent authors of research papers on the arXiv 
in the General Relativity and Quantum Cosmology section. 
There is an edge between two authors if they have co-authored at least one paper together. 
Note that some edges may appear twice in the data, once for each direction. 
Ignoring repeats and self-edges, there are 5242 nodes and 14484 edges. 
(Note: Repeats are automatically ignored when loading an (un)directed graph with 
SNAP’s LoadEdgeList function). """

#Preprocessing the collab network. GetEdges() did not remove self edges 
collab_network = snap.LoadEdgeList(snap.PUNGraph,"CA-GrQc.txt")

#Code to remove self edges
self_edge_nodes = 0
for edge in collab_network.Edges():
   if edge.GetSrcNId() == edge.GetDstNId():
      src = edge.GetSrcNId()
      dst = edge.GetDstNId()
      collab_network.DelEdge(src,dst)

""" Question 1.1 - Plot the degree distribution of all three networks in the same plot on a
log-log scale. In other words, generate a plot with the horizontal axis 
representing node degrees and the vertical axis representing the proportion of nodes 
with a given degree (by “log-log scale” we mean that both the horizontal and vertical axis 
must be in logarithmic scale). In one to two sentences, describe one key difference 
between the degree distribution of the collaboration network and the 
degree distributions of the random graph models. """


def generate_x_y(graph):
    #update the degrees for the random graph/network
    for node in graph:
        node.degree = len(node.neighbors)
    x_list = []
    for node in graph:
        x_list.append(node.degree)
    counter=collections.Counter(x_list)
    x = [a for a in counter.keys()] # node degrees
    tmp = counter.values() # frequency
    y = [(x/5242)*100 for x in tmp]
    return counter,x,y

# Produce instance of and generate x,y for Erdos-Renyi Random graph
print("Generating erdos-renyi random graph with n=5242,m=14484 and p=0.5...")
erdos_renyi_graph = er_randomGraph(5242,14484,0.5)
erdos_counter, erdos_x, erdos_y = generate_x_y(erdos_renyi_graph)
print("After processing erdos-renyi graph, we have")
print("Counter of the form degree:count",erdos_counter,"\n x axis ",erdos_x,"\n y axis",erdos_y)
plt.loglog(erdos_x, erdos_y, color = 'y', label = 'Erdos Renyi Network')

# Produce instance of and generate x,y for Small-World Random Network
print("\nGenerating smallworld network with n=5242")
small_world_graph = sw_randomGraph(5242)
small_world_counter,small_world_x, small_world_y = generate_x_y(small_world_graph)
print("After processing small world network, we have")
print("Counter of the form degree:count",small_world_counter,"\n x axis ",small_world_x,"\n y axis",small_world_y)
plt.loglog(small_world_x, small_world_y, linestyle = 'dashed',color = 'r', label = 'Small World Network')

# Generate x,y for Collab network
collab_deg_list = []
for node in collab_network.Nodes():
    collab_deg_list.append(node.GetDeg())
counter=collections.Counter(collab_deg_list)
collab_x = [a for a in counter.keys()] # node degrees
tmp = counter.values() # frequency
collab_y = [(x/5242)*100 for x in tmp]
plt.loglog(collab_x, collab_y, linestyle = 'dotted',color = 'g', label = 'Collab Network')

plt.xlabel('Node Degree (log)')
plt.ylabel('Proportion of Nodes with a Given Degree (log)')
plt.title('Degree Distribution of Erdos Renyi, Small World, and Collaboration Networks')
plt.legend()
plt.savefig("out.png")
#plt.show()
