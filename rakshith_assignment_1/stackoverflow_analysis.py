# Rakshith Singh Assignment 1 - Stackoverflow Analysis
# https://snap.stanford.edu/snappy/doc/reference/index-ref.html
# https://stackoverflow.com/questions/10152131/how-do-i-index-the-3-highest-values-in-a-list
import snap
stackoverflow_graph = snap.LoadEdgeList(snap.PNGraph,"stackoverflow-Java.txt")

#Question 1 - The number of weakly connected components in the network.
Components = snap.TCnComV()
snap.GetWccs(stackoverflow_graph, Components)
print("Number of weakly connected components is ",len(Components))

#Question 2 - The number of edges and the number of nodes in the largest weakly connected component.
MxWcc = snap.GetMxWcc(stackoverflow_graph)
print("The number of nodes in the largest Wcc is ",MxWcc.GetNodes())
print("The number of edges in the largest Wcc is ",MxWcc.GetEdges())

#Question 3 - The top 3 most central nodes in the network by PagePank scores.
PRankH = snap.TIntFltH()
snap.GetPageRank(stackoverflow_graph, PRankH)
first = 3496478
second = 3600470
third = 3399766
#for item in PRankH:
#    print(item, PRankH[item])
node_list = []
prank_list = []
for item in PRankH:
	node_list.append(item)
	prank_list.append(PRankH[item])
results = sorted(zip(prank_list, node_list), reverse=True)[:3]
print("Top 3 Central nodes and their Page Ranks are")
for result in results:
	a,b = result
	print(b,a)

#Question 4 - The top 3 hubs and top 3 authorities in the network by HITS scores.
NIdHubH = snap.TIntFltH()
NIdAuthH = snap.TIntFltH()
snap.GetHits(stackoverflow_graph, NIdHubH, NIdAuthH)
tmp_lst1 = []
tmp_lst2 = []
for item in NIdHubH:
	tmp_lst1.append(item)
	tmp_lst2.append(NIdHubH[item])
hub_results = sorted(zip(tmp_lst2, tmp_lst1), reverse=True)[:3]

tmp_lst3 = []
tmp_lst4 = []
for item in NIdAuthH:
	tmp_lst3.append(item)
	tmp_lst4.append(NIdAuthH[item])
auth_results = sorted(zip(tmp_lst4, tmp_lst3), reverse=True)[:3]

print("Top 3 Hubs and their hit scores are")
for result in hub_results:
        p,q = result
        print(q,p)

print("Top 3 Authorities and their hit scores are")
for result in auth_results:
        x,y = result
        print(y,x)
