# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 14:14:17 2016

@author: U6038155
"""

import numpy as np
from sklearn import cluster
import networkx as nx

def agg_cluster1(G): # pass in a nx object
    distances=np.zeros((len(G),len(G)))
    distances.fill(0.0)

    for edge in G.edges():
        i = edge[0]
        j = edge[1]
        distances[i][j]=1
        distances[j][i]=1
    for n in xrange(G.size()):
       # print n
        distances[n][n]=2
        
    x, clabels = cluster.affinity_propagation(distances)
    res= {"centroids":x , "labels":clabels }
    return res

G = nx.Graph()

# Populate GLink graph

for i in xrange(10):
    G.add_node(i)

GDict = {0:[1],1:[0,2,3,4,5],2:[1],3:[1],4:[1],5:[1,6],6:[5,7,8],7:[6],8:[6]}

if __name__ == "__main__":   
    
    for key, val in GDict.iteritems():
        for v in val:        
            G.add_edge(key,v)
            
    close = nx.closeness_vitality(G)
    print close
    
    hubs = agg_cluster1(G)
    print hubs
