import networkx as nx
import matplotlib.pyplot as plt
import seaborn
from networkx.algorithms import bipartite
import pandas as pd
import numpy as np
import statistics
import seaborn as sns;

sns.set()
from sklearn.linear_model import LinearRegression


# Create subgraph :
def createGraph(file):
    # Open file and read all lines
    file1 = open(file, 'r')
    Lines = file1.readlines()
    i = 0
    names = []
    crimes = []
    matrix = []

    # line.strip() holds the current line and remove newline character
    for line in Lines:
        stripped_line = line.strip()
        stripped_line = stripped_line.replace("", '')
        if 3 < i < 874:
            names.append(stripped_line)
        elif 874 < i < 557 + 875:
            crimes.append(stripped_line)
        else:
            if i > 557 + 875:
                matrix.append(stripped_line.split())
        i += 1

    df = pd.DataFrame(data=matrix, index=names, columns=crimes)
    # print(df.tail())

    # Making the bipartie graph
    B = nx.Graph()
    i = 0
    j = 0
    count = 0
    for name in names:
        for crime in crimes:
            if matrix[i][j] != '0':
                B.add_node(name, bipartite=0)
                B.add_node(crime, bipartite=1)
                B.add_edge(name, crime)

            j += 1
        # if i == 10:
        #   break
        i += 1
        j = 0
    # nx.draw(B, with_labels=True, font_size=6, node_color='yellowgreen', node_size=10)
    # plt.show()
    return B, matrix, names, crimes


# Create graph :
def createSubGraph(listSubgraph, color):
    G = nx.Graph()
    for indiv, idCrime in listSubgraph:
        G.add_node(indiv, bipartite=0)
        G.add_node(idCrime, bipartite=1)
        G.add_edge(indiv, idCrime)
    # nx.draw(G, with_labels=True, font_size=6, node_color=color, node_size=10)
    # plt.show()
    return G


# Plot degree histogram :
def plot_degree_hist(G, grapheName):
    degrees = [G.degree(n) for n in G.nodes()]

    plt.title("Degree histogram of graph: " + str(grapheName))
    plt.ylabel('Frequency')
    plt.xlabel('Degree')

    plt.hist(degrees)
    plt.show()


# Plot degree distribution histogram and power law :
def plot_degree_distrbution(degrees, colorBar, grapheName):
    # Calculate degree distribution :
    minDegree = min(degrees)
    maxDegree = max(degrees)
    dist = []
    for element in range(minDegree, maxDegree + 1):
        if degrees.count(element) != 0:
            dist.append([element, degrees.count(element)])

    totalNodes = sum([pair[1] for pair in dist])
    degreeProba = []

    for i, j in dist:
        proba = j / totalNodes
        degreeProba.append([i, proba])

    listeDegrees = [pair[0] for pair in degreeProba]
    frequency = [pair[1] for pair in degreeProba]
    plt.title("Degree distribution of " + str(grapheName))
    plt.ylabel('log(Probability)')
    plt.xlabel('log(Degree)')
    xlog = np.log(listeDegrees)
    ylog = np.log(frequency)
    seaborn.regplot(xlog, ylog, x_ci=95, color='red', label ="Power law")
    plt.scatter(np.log(listeDegrees), np.log(frequency), color=colorBar, label="Degree distribution")
    plt.legend(loc='best')
    plt.show()
    return degreeProba, dist


# Plot Degree distribution heat map :
def plot_heat_map(matrixDist, dist, title):
    # plt.imshow(matrixDist, cmap='hot', interpolation='nearest')
    # plt.show()
    "Draw the heatmap for crimes "
    plt.title("Heatmap for " + str(title))
    listeDegrees = [pair[0] for pair in matrixDist]
    count = [pair[1] for pair in dist]
    df = pd.DataFrame(data=listeDegrees, index=count, columns=['Degree distribution'])
    ax = sns.heatmap(df)
    plt.show()


# Plot Degree distribution power law  :
def plot_Log_Log(matrixDist, title):
    listeDegrees = [pair[0] for pair in matrixDist]
    frequency = [pair[1] for pair in matrixDist]
    xlog = np.log(listeDegrees)
    ylog = np.log(frequency)
    reg = LinearRegression().fit(xlog, ylog)
    yp = reg.predict(xlog)
    ax = plt.gca()
    plt.plot(xlog, ylog, linewidth=2.5, color='navy', label=r'$f(x) = 3.5\cdot x + \ln(30)$')
    plt.legend(loc='best')
    plt.xlabel(r'log(Degree)')
    plt.ylabel(r'log(Frequency)')
    ax.grid(True)
    plt.title(r'Power law plot for ' + str(title))
    plt.show()
    plt.clf()


# Python program to get average of a list 
def Average(lst):
    return statistics.mean(lst)


# maximum degree centrality,
def max_degree_centrality(G):
    return max(nx.degree_centrality(G).values()) * G.number_of_nodes()


# minimum degree centrality,
def min_degree_centrality(G):
    return min(nx.degree_centrality(G).values()) * G.number_of_nodes()


# average In-betweeness centrality
def Average_betweeness_centrality(G):
    betweeness_centrality_normalized = nx.betweenness_centrality(G, weight=None, normalized=True)
    return Average(betweeness_centrality_normalized.values())


# In-betweeness centrality  variance
def Variance_betweeness_centrality(G):
    betweeness_centrality_normalized = nx.betweenness_centrality(G, weight=None, normalized=True)
    return statistics.variance(betweeness_centrality_normalized.values())


# average path length
def Average_path_length(G):
    paths = []
    for g in nx.connected_components(G):
        S = G.subgraph(g)
        paths.append(nx.average_shortest_path_length(S))

    return sum(paths) / len(paths)


# clustering coefficient,

# Average Degree centrality
def AverageDegreeCentrality(G):
    return Average(nx.degree_centrality(G).values())


# calculate the variance
def VarianceDegreeCentrality(G):
    return statistics.variance(nx.degree_centrality(G).values())


# Maximum degree :
def MaxDegree(G, dexX, degY):
    # print(nx.is_bipartite(B))

    maxi = 0
    name = ""
    for el in list(dexX):
        if el[1] > maxi:
            maxi = el[1]
            name = el[0]
    print("Maximum degree (individuals) -->  ", maxi, name)

    maxi = 0
    crime = ""
    for el in list(degY):
        if el[1] > maxi:
            maxi = el[1]
            crime = el[0]
    print("Maximum degree (crimes) -->  ", maxi, crime)


# Minimum degree :
def MinDegree(G, dexX, degY):
    mini = float("inf")
    name = ""
    for el in list(dexX):
        if el[1] < mini:
            mini = el[1]
            name = el[0]
    print("Minimum degree (individuals) -->  ", mini, name)

    mini = float("inf")
    crime = ""
    for el in list(degY):
        if el[1] < mini:
            mini = el[1]
            crime = el[0]
    print("Minimum degree (crimes) -->  ", mini, crime)


# Size of giant component :
def GiantComponent(G):
    largest_cc = max(nx.connected_components(G), key=len)
    S = G.subgraph(largest_cc)

    # nx.draw(S, with_labels=True, font_size=6, node_color='yellowgreen', node_size=10)
    top_nodes = {n for n, d in S.nodes(data=True) if d['bipartite'] == 0}
    bottom_nodes = set(S) - top_nodes
    dexX, degY = bipartite.degrees(S, bottom_nodes)

    return S, len(dexX), len(degY), nx.number_of_nodes(S)


# Diameter :
def Diameter(G):
    diameters = []
    for c in nx.connected_components(G):
        S = G.subgraph(c)
        diameters.append(nx.diameter(S))
    print("Diameter : ", max(diameters))


# Average shortest path length :
def AvgShortPath(G):
    paths = []
    for g in nx.connected_components(G):
        S = G.subgraph(g)
        paths.append(nx.average_shortest_path_length(S))

    return sum(paths) / len(paths), paths


def VarianceAvg(avg):
    return statistics.variance(avg)


# Calculate global attributes :
def GlobalAttr(G):
    print("Average Degree Centrality -->  ", AverageDegreeCentrality(G))
    print("Variance Degree Centrality -->  ", VarianceDegreeCentrality(G))

    top_nodes = {n for n, d in G.nodes(data=True) if d['bipartite'] == 0}
    bottom_nodes = set(G) - top_nodes
    dexX, degY = bipartite.degrees(G, bottom_nodes)

    MaxDegree(G, dexX, degY)
    MinDegree(G, dexX, degY)
    S, X, Y, n = GiantComponent(G)
    print("Number of nodes of the giant component : ", n)
    Diameter(G)
    AvgShortPath(G)
    print("Clustering coefficient --> {}".format(nx.algorithms.cluster.transitivity(G)))
