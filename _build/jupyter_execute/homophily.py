#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import NetworkX and key data science libraries
import networkx as nx
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme()


# In[2]:


edges = pd.read_csv("quaker-edges.csv")
edges


# In[3]:


nodes = pd.read_csv("quaker-nodes.csv")
nodes


# In[4]:


quakers = nx.from_pandas_edgelist(edges, source="Source", target="Target")
print(quakers)


# In[5]:


p = nodes.groupby("gender").count().Id["male"]/nodes.count().Id
p


# In[6]:


q = nodes.groupby("gender").count().Id["female"]/nodes.count().Id
q


# In[7]:


2*p*q


# In[8]:


nx.set_node_attributes(quakers, dict(zip(nodes.Id, nodes.gender)), 'gender')


# In[9]:


mixed_edges = len([(s,t) for s,t in quakers.edges if quakers.nodes[s]['gender'] != quakers.nodes[t]['gender']])
mixed_edges


# In[10]:


mixed_edges/quakers.number_of_edges()


# In[31]:


def homophily(mixed_edges):
    return 2*p*q - mixed_edges/quakers.number_of_edges()


# In[32]:


obs_homophily = homophily(mixed_edges)
obs_homophily


# In[16]:


def simulate_mixed_edges(data, attribute, id_attr, graph):
    attr_column = data[attribute].sample(frac=1).reset_index(drop=True) # Reshuffle column
    nx.set_node_attributes(graph, dict(zip(data[id_attr], attr_column)), attribute) # Set node attribute
    mixed_edges = len([(s,t) for s,t in graph.edges if graph.nodes[s][attribute] != graph.nodes[t][attribute]]) # Get number of mixed edges
    return mixed_edges


# In[33]:


sim_homophily = pd.Series([homophily(simulate_mixed_edges(nodes, 'gender', 'Id', quakers)) for i in range(5000)])
sim_homophily


# In[34]:


plt = sns.histplot(x=sim_homophily)
plt.axvline(x=obs_homophily, color="red", ls="--")


# In[35]:


p_value = np.mean(sim_homophily > obs_homophily)
p_value

