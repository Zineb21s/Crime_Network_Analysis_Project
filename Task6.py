from bib import *
from networkx.algorithms.core import k_core
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
            if value == '1':
                victims.append([names[i], crimes[j]])
            elif value == '2':
                suspects.append([names[i], crimes[j]])


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


crimesIDVic = [pair[1] for pair in victims]
crimesIDSus = [pair[1] for pair in suspects]

crimesIDIntrs = intersection(crimesIDVic, crimesIDSus)

triple = []
for element in crimesIDIntrs:
    id1 = crimesIDVic.index(element)
    id2 = crimesIDSus.index(element)
    triple.append([victims[id1][0], suspects[id2][0], element])

nodes = [[pair[0], pair[1]] for pair in triple]

B = createSubGraph(nodes, 'yellowgreen')
" K-cores and K-plex "
KGraph = k_core(B)
nx.draw(KGraph, with_labels=True, font_size=6, node_color='yellowgreen', node_size=10)
plt.show()