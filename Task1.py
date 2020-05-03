from bib import *
from networkx.algorithms import bipartite

file = 'crime.txt'
G, matrix, names, crimes = createGraph(file)

print("Average Degree Centrality -->  ", AverageDegreeCentrality(G))
print("Variance Degree Centrality -->  ", VarianceDegreeCentrality(G))

top_nodes = {n for n, d in G.nodes(data=True) if d['bipartite'] == 0}
bottom_nodes = set(G) - top_nodes
dexX, degY = bipartite.degrees(G, bottom_nodes)

MaxDegree(G,dexX,degY)
MinDegree(G,dexX,degY)
avg,paths =AvgShortPath(G)
print("Average path length --> ", avg)
S , X , Y , n  = GiantComponent(G)
print("Number of nodes (individuals) of the giant component --> ", X)
print("Number of nodes (crimes) of the giant component --> ", Y)
Diameter(G)


#GlobalAttr(G)