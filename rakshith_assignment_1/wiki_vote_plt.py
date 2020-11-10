#Rakshith Singh Assignment 1 Log-Log Plot
import snap

wiki_graph = snap.LoadEdgeList(snap.PNGraph,"wiki-Vote.txt")
number_nodes = wiki_graph.GetNodes()
#print ("Question 1 - Number of Nodes in the graph is ",number_nodes)

out_degree_list = []
for node in wiki_graph.Nodes():
    if node.GetOutDeg() != 0:
        out_degree_list.append(node.GetOutDeg())

# code to group items in list by frequency https://www.geeksforgeeks.org/python-group-list-elements-based-on-frequency/
from collections import Counter
def group_list(lst):
    return list(zip(Counter(lst).keys(), Counter(lst).values()))
result = group_list(out_degree_list)

x = []
y = []

for data in result:
    a, b = data
    x.append(a)
    y.append(b)

# code to plot log-log graph https://www.kite.com/python/docs/matplotlib.pyplot.loglog
import matplotlib.pyplot as plt
plt.loglog(x, y)
plt.savefig("out.png")
