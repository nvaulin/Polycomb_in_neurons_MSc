import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.lines import Line2D

import networkx as nx


def draw_network(G, k=1.3, seed=42, layout='neato', pos=None, chroms_colors=None):    
    assert pos is not None
    assert chroms_colors is not None
    nodes_colors = np.array([chroms_colors[w] for *_, w in G.nodes.data('Chromosome')])
    nx.draw_networkx_nodes(G, pos, node_size=20, node_color=nodes_colors, linewidths=1,edgecolors='k')
    nx.draw_networkx_edges(G, pos, width=1)

    ax = plt.gca()
    ax.margins(0.08)
    handles = [Line2D([0], [0], marker='o', color='w', label=label, mfc=color, ms=5, mec='k') for label, color in chroms_colors.items()]
    ax.legend(handles=handles[:-1], ncols=1, frameon=False, loc ='upper left', bbox_to_anchor=(.99, .9), prop={'size':5})
    plt.axis("off");
    
def get_cliques(cliques, size=2):
    processed_cliques = set()
    
    for clique in cliques:
        if len(clique) >= size:
            processed_clique = frozenset(sorted(clique))
            if processed_clique not in processed_cliques:
                processed_cliques.add(processed_clique)
                yield clique