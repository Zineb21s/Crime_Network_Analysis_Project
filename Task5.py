import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
import pandas as pd
import numpy as np
from bib import * 
import statistics 



# Task 5 ***************

# Create graph 
file = 'crime.txt'
G, matrix, names, crimes = createGraph(file)


top_nodes = {n for n, d in G.nodes(data=True) if d['bipartite'] == 0}  # indiv
bottom_nodes = set(G) - top_nodes


victims = []
suspects = []

indivs = len(matrix)
nbrCrimes = len(matrix[0])

for i in range(indivs):
    for j in range(nbrCrimes):
          value = matrix[i][j]
          if value != '0':
              if   value == '1':
                 victims.append([names[i],crimes[j]])
              elif value == '2':
                 suspects.append([names[i],crimes[j]])

def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 

crimesIDVic = [pair[1] for pair in victims]
crimesIDSus = [pair[1] for pair in suspects]

crimesIDIntrs = intersection(crimesIDVic, crimesIDSus)

triple = []
for element in crimesIDIntrs:
    id1 = crimesIDVic.index(element)
    id2 = crimesIDSus.index(element)
    triple.append([victims[id1][0],suspects[id2][0],element])
    

nodes = [[pair[0],pair[1]] for pair in triple]

#print(triple)

B = createSubGraph(nodes,'yellowgreen')

nx.draw(B, with_labels=False, font_size=6, node_color='yellowgreen', node_size=10)
plt.show()

GlobalAttr(B)
degrees = [B.degree(n) for n in B.nodes()]
degreeProbaV = plot_degree_distrbution(degrees,'blue', 'Victims')
#plot_Log_Log(degreeProbaV, "Victims")

print("Minimum Degree Centrality -->  ",min_degree_centrality(G))
print("Maximum Degree Centrality -->  ",max_degree_centrality(G))
print("Average betweeness Degree Centrality -->  ",Average_betweeness_centrality(B))
print("Variance betweeness Degree Centrality -->  ",Variance_betweeness_centrality(B))
average , paths = AvgShortPath(B)
print("Average path length --> ", average)
print("Variance of average path length --> ", VarianceAvg(paths))


