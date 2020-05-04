import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
import collections
import seaborn as sns; sns.set()
import pandas as pd

# Opens file and reads all lines
file1 = open('crime.txt', 'r')
Lines = file1.readlines()
i = 0
names = []
crimes = []
matrix = []

# line.strip() holds the current line and removes newline character
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

# df = pd.DataFrame(data=matrix, index=names, columns=crimes)
# print(df.tail())

" Making the bipartite graph "
B = nx.Graph()
i = 0
j = 0
count = 0
for name in names:
    for crime in crimes:
        if matrix[i][j] != '0':
            # print("This i : ", i, "This j ", j , "name : " , name, crime)
            B.add_node(name, bipartite=0)
            B.add_node(crime, bipartite=1)
            B.add_edge(names[i], crimes[j])
            # pos = layout(B)

        j += 1
    # if i == 10:
    #   break
    i += 1
    j = 0

top_nodes = {n for n, d in B.nodes(data=True) if d['bipartite'] == 0}
bottom_nodes = set(B) - top_nodes
dexX, degY = bipartite.degrees(B, bottom_nodes)

" Draw the cumulative degree distribution for indivuals "
degrees = []
for d in dexX:
    degrees.append(d[1])

degreeCount = collections.Counter(sorted(degrees))
deg, cnt = zip(*degreeCount.items())
fig, ax = plt.subplots()
proba = []

for d in deg:
    c = 0
    for degree in degrees:
        if degree >= d:
            c += 1
    proba.append(c)

plt.plot(deg, proba, c='blue')
plt.title("Cumulative Degree for individuals")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d for d in deg])
ax.set_xticklabels(deg)
plt.show()

"Draw the heatmap for individuals "
plt.title("Heatmap for individuals")
df = pd.DataFrame(data=deg, index=proba, columns=['individuals'])
ax = sns.heatmap(df)
plt.show()

" Draw the cumulative degree distribution for crimes "
degreesY = []
for d in degY:
    degreesY.append(d[1])
proba = []
degreeCount = collections.Counter(sorted(degreesY))
deg, cnt = zip(*degreeCount.items())

for d in deg:
    c = 0
    for degree in degreesY:
        if degree >= d:
            c += 1
    proba.append(c)

fig, ax = plt.subplots()
plt.plot(deg, proba, c='blue')
plt.title("Cumulative Degree for crimes")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d for d in deg])
ax.set_xticklabels(deg)
plt.show()

"Draw the heatmap for crimes "
plt.title("Heatmap for crimes")
df = pd.DataFrame(data=deg, index=proba, columns=['crimes'])
ax = sns.heatmap(df)
print(len(deg))
#nx.draw(B, with_labels=False, font_size=6, node_size=20, node_color=proba, cmap=plt.cm.magma)

plt.show()
