import networkx as nx
from bib import *
import collections

# Task 7 ***************

# Create graph 
file = 'crime.txt'
G, matrix, names, crimes = createGraph(file)

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


B = createSubGraph(nodes,'yellowgreen')

#nx.draw(B, with_labels=True, font_size=6, node_color='yellowgreen', node_size=10)
#plt.show()

loc_c_coeffs = nx.clustering(B)
clusteringCount = collections.Counter(sorted(list(loc_c_coeffs.values())))
clu, cnt = zip(*clusteringCount.items())
fig, ax = plt.subplots()
plt.plot(clu, cnt, c='blue')
plt.title("Individual clustering coefficients")
plt.ylabel("Count")
plt.xlabel("Local clustering coefficient")
ax.set_xticks([d for d in clu])
ax.set_xticklabels(clu)
print(clusteringCount)
plt.show()
plt.clf()

plt.title("Individual clustering coefficients")
cluster_values = list(nx.clustering(B).values())
nx.draw(B, with_labels=False, font_size=6, node_size=20, node_color=cluster_values, cmap=plt.cm.magma)
sm = plt.cm.ScalarMappable(cmap=plt.cm.magma, norm=plt.Normalize(vmin = min(cluster_values), vmax=max(cluster_values)))
plt.colorbar(sm)
plt.show()
plt.clf()