import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
import pandas as pd
import numpy as np
from bib import * 


# Create graph 
file = 'crime.txt'
G, matrix, names, crimes = createGraph(file)

# Task 3 ****************

# Plot degree distribution and power law for individuals
top_nodes = {n for n, d in G.nodes(data=True) if d['bipartite'] == 0}
bottom_nodes = set(G) - top_nodes
dexX, degY = bipartite.degrees(G, bottom_nodes)
degrees = []
for el in list(dexX):
        degrees.append(el[1])

degreeProba, dist = plot_degree_distrbution(degrees,'blue', 'Individuals')

# Plot Degree distribution heat map for individuals
plot_heat_map(degreeProba, dist,"Individuals")


# Plot degree distribution and power law for crimes
degrees = []
for el in list(degY):
        degrees.append(el[1])
degreeProba, dist = plot_degree_distrbution(degrees,'blue', 'Crimes')

# Plot Degree distribution heat map for crimes
plot_heat_map(degreeProba, dist,"Crimes")





