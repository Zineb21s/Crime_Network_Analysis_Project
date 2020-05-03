from bib import *
import collections
import networkx as nx
from networkx.algorithms.core import k_core

# Task 8 ***************

# Create graph 
file = 'crime.txt'
G, matrix, names, crimes = createGraph(file)

victims = []
suspects = []
witnesses = []

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
            elif value == '3':
                witnesses.append([names[i], crimes[j]])


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


crimesIDVic = [pair[1] for pair in victims]
crimesIDSus = [pair[1] for pair in suspects]
crimesIDWit = [pair[1] for pair in witnesses]


def createIntersectingSubgraph(first_id, second_id, first_titles, second_titles):
    crimesIDIntrs = intersection(first_id, second_id)
    triple = []
    for element in crimesIDIntrs:
        id1 = first_id.index(element)
        id2 = second_id.index(element)
        triple.append([first_titles[id1][0], second_titles[id2][0], element])
    nodes = [[pair[0], pair[1]] for pair in triple]
    return createSubGraph(nodes, 'yellowgreen')


vic_wit_G = createIntersectingSubgraph(crimesIDVic, crimesIDWit, victims, witnesses)
sus_wit_G = createIntersectingSubgraph(crimesIDSus, crimesIDWit, suspects, witnesses)


# nx.draw(vic_wit_G, with_labels=True, font_size=6, node_color='yellowgreen', node_size=10)
# plt.show()

# nx.draw(sus_wit_G, with_labels=True, font_size=6, node_color='yellowgreen', node_size=10)
# plt.show()

def run_task5(X, title):
    GlobalAttr(X)
    degrees = [X.degree(n) for n in X.nodes()]
    degreeProbaV = plot_degree_distrbution(degrees, 'blue', title)
    print("Minimum Degree Centrality -->  ", min_degree_centrality(G))
    print("Maximum Degree Centrality -->  ", max_degree_centrality(G))
    print("Average betweeness Degree Centrality -->  ", Average_betweeness_centrality(G))
    print("Variance betweeness Degree Centrality -->  ", Variance_betweeness_centrality(G))
    average, paths = AvgShortPath(G)
    print("Average path length --> ", average)
    print("Variance of average path length --> ", VarianceAvg(paths))

    # print("Average path length -->  ",Average_path_length(X))


def run_task6(X, title):
    # print(X)
    KGraph = k_core(X, 1)
    # print(KGraph)
    nx.draw(KGraph, with_labels=True, font_size=6, node_color='yellowgreen', node_size=10)
    plt.show()
    plt.clf()


def run_task7(X, title):
    loc_c_coeffs = nx.clustering(X)
    clusteringCount = collections.Counter(sorted(list(loc_c_coeffs.values())))
    clu, cnt = zip(*clusteringCount.items())
    fig, ax = plt.subplots()
    plt.plot(clu, cnt, c='blue')
    plt.title("Individual clustering coefficients for " + title)
    plt.ylabel("Count")
    plt.xlabel("Local clustering coefficient")
    ax.set_xticks([d for d in clu])
    ax.set_xticklabels(clu)
    print(clusteringCount)
    plt.show()
    plt.clf()

    plt.title("Individual clustering coefficients for " + title)
    cluster_values = list(nx.clustering(X).values())
    nx.draw(X, with_labels=False, font_size=6, node_size=20, node_color=cluster_values, cmap=plt.cm.magma)
    sm = plt.cm.ScalarMappable(cmap=plt.cm.magma,
                               norm=plt.Normalize(vmin=min(cluster_values), vmax=max(cluster_values)))
    plt.colorbar(sm)
    nx.draw(X, with_labels=False, font_size=6, node_size=20, node_color=list(nx.clustering(X).values()),
            cmap=plt.cm.magma)
    plt.show()
    plt.clf()


print("\nVictims-Witnesses\n")
run_task5(vic_wit_G, "Victims-Witnesses")
run_task6(vic_wit_G, "Victims-Witnesses")
run_task7(vic_wit_G, "Victims-Witnesses")

print("\nSuspects-Witnesses\n")
run_task5(sus_wit_G, "Suspects-Witnesses")
run_task6(sus_wit_G, "Suspects-Witnesses")
run_task7(sus_wit_G, "Suspects-Witnesses")