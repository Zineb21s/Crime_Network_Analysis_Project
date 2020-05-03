import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
import pandas as pd
import numpy as np
from bib import * 


# Task 4 ***************

# Create graph 
file = 'crime.txt'
G, matrix, names, crimes = createGraph(file)


# Create subgraphs
victims = []
suspects = []
witnesses = []
dual = []

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
              elif value == '3':
                  witnesses.append([names[i],crimes[j]])
              elif value == '4':
                   dual.append([names[i],crimes[j]]) 


VictimsGraph = createSubGraph(victims,'yellowgreen')
SuspectsGraph = createSubGraph(suspects,'yellowgreen')
WitnessesGraph = createSubGraph(witnesses,'yellowgreen')
DualGraph= createSubGraph(dual,'yellowgreen')
   

# Plot degree distribution histogram for subgraphs and calculate global attributes

print("-------------------------- Calculate global attributes for graph victimes : --------------------------")
GlobalAttr(VictimsGraph)
degrees = [VictimsGraph.degree(n) for n in VictimsGraph.nodes()]
degreeProbaV, dist1 = plot_degree_distrbution(degrees,'blue', 'Victimes')
#plot_Log_Log(degreeProbaV, "Victimes")

print("-------------------------- Calculate global attributes for graph suspects : --------------------------")
GlobalAttr(SuspectsGraph)
nx.draw(SuspectsGraph, with_labels=True, font_size=6, node_color='yellowgreen', node_size=10)
plt.show()
degrees = [SuspectsGraph.degree(n) for n in SuspectsGraph.nodes()]
degreeProbaS, dist2 = plot_degree_distrbution(degrees,'green', 'Suspects')
#plot_Log_Log(degreeProbaS, "Suspects")

print("-------------------------- Calculate global attributes for graph witnesses : --------------------------")
GlobalAttr(WitnessesGraph)
degrees = [WitnessesGraph.degree(n) for n in WitnessesGraph.nodes()]
degreeProbaW, dist3 = plot_degree_distrbution(degrees,'black', 'Witnesses')
#plot_Log_Log(degreeProbaW,"Witnesses")

print("-------------------------- Calculate global attributes for graph duals : --------------------------")
GlobalAttr(DualGraph)
degrees = [DualGraph.degree(n) for n in DualGraph.nodes()]
degreeProbaD, dist4 = plot_degree_distrbution(degrees,'cyan', 'Duals')
#plot_Log_Log(degreeProbaD,"Duals")
