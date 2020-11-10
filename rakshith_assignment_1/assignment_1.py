# Rakshith Singh Assignment 1

import snap

#Helper function
def graph_info(graph):
    for node in graph.Nodes():
        print("node id",node.GetId()," out degree ",node.GetOutDeg()," in degree ", node.GetInDeg())

wiki_graph = snap.LoadEdgeList(snap.PNGraph,"wiki-Vote.txt")
#graph_info(wiki_graph)

#Question 1 - The number of nodes in the network
number_nodes = wiki_graph.GetNodes()
print ("Question 1 - Number of Nodes in the graph is ",number_nodes)

#Question 2 - The number of nodes with a self-edge (self-loop)
self_edge_nodes = 0
for edge in wiki_graph.Edges():
    if edge.GetSrcNId() == edge.GetDstNId():
        self_edge_nodes+=1
print("Question 2 - Number of Nodes with a self loop is ", self_edge_nodes)

#Question 3 - The number of directed edges in the network
directed_edges  = wiki_graph.GetEdges()
print("Question 3 - Number of directed edges is ", directed_edges)

#Question 4 - The number of undirected edges in the network
undirected_edges = 0
node_id_list = []
for node in wiki_graph.Nodes():
    node_id_list.append(node.GetId())
for i in node_id_list:
    for j in node_id_list:
        if wiki_graph.IsEdge(i,j):
            undirected_edges+=1
            node_id_list.remove(j)
print("Question 4 - Number of undirected edges is ", undirected_edges)

#Question 5 - The number of reciprocated edges in the network
reciprocated_edges = 0
new_node_id_list = []
for node in wiki_graph.Nodes():
    new_node_id_list.append(node.GetId())
for i in new_node_id_list:
    for j in new_node_id_list:
        if wiki_graph.IsEdge(i,j) and wiki_graph.IsEdge(j,i):
            reciprocated_edges+=1
print("Question 5 - Number of reciprocated edges is ", reciprocated_edges)

#Question 6 - The number of nodes of zero out-degree
zero_out_degree_nodes = 0
for node in wiki_graph.Nodes():
        if node.GetOutDeg() == 0:
            zero_out_degree_nodes+=1
print("Question 6 - Number of nodes with 0 out-degree is ", zero_out_degree_nodes)

#Question 7 - The number of nodes of zero in-degree
zero_in_degree_nodes = 0
for node in wiki_graph.Nodes():
        if node.GetInDeg() == 0:
            zero_in_degree_nodes+=1
print("Question 7 - Number of nodes with zero in-degree is ", zero_in_degree_nodes)

#Question 8 - The number of nodes with more than 10 outgoing edges
ten_plus_out_degree_nodes = 0
for node in wiki_graph.Nodes():
        if node.GetOutDeg() > 10:
            ten_plus_out_degree_nodes+=1
print("Question 8 - Number of nodes with out-degree > 10 is ", ten_plus_out_degree_nodes)

#Question 9 - The number of nodes with fewer than 10 incoming edges
less_ten_in_degree_nodes = 0
for node in wiki_graph.Nodes():
        if node.GetInDeg() < 10:
            less_ten_in_degree_nodes+=1
print("Question 9 - Number of nodes with in-degree < 10 is ", less_ten_in_degree_nodes)

