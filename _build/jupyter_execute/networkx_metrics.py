#!/usr/bin/env python
# coding: utf-8

# # Basic Network Metrics with NetworkX
# 
# This reference sheet includes some basic NetworkX functions, for understanding paths, directedness, and components. It uses the [Marvel network](https://github.com/melaniewalsh/sample-social-network-datasets/tree/master/sample-datasets/marvel) data as an example.
# 
# ## Importing a Graph object

# In[1]:


# Import NetworkX and key data science libraries
import networkx as nx
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme()


# We already explored some methods for importing network data in a previous class, but sometimes importing data as a CSV can be tricky. In these cases, it's often easier to use pandas to import the data, and then convert from there:

# (There's plenty of information on [Pandas](https://pandas.pydata.org/docs/user_guide/index.html) and [Seaborn](https://seaborn.pydata.org/tutorial.html) available in their documentation, too!)

# In[2]:


marvel_pd = pd.read_csv("marvel-unimodal-edges.csv")
marvel = nx.from_pandas_edgelist(marvel_pd, source="Source", target="Target", edge_attr=True)
print(marvel)


# ## The Basics

# In[3]:


len(marvel.nodes) # Number of nodes


# In[4]:


len(marvel.edges) # Number of edges


# In[5]:


marvel.number_of_edges() # Alternative method for number of edges


# In[6]:


marvel.is_directed() # Is the graph directed?


# ## Paths

# In[7]:


nx.shortest_path(marvel, "Black Panther / T'chal", 	"Gambit / Remy Lebeau") # Shortest path as list


# In[8]:


nx.shortest_path_length(marvel, "Black Panther / T'chal", "Gambit / Remy Lebeau") #Shortest path length (Distance)


# In[9]:


nx.average_shortest_path_length(marvel) # Average shortest path length (Average distance)


# In[10]:


nx.diameter(marvel)


# # Components

# In[11]:


nx.is_connected(marvel) # Is the graph connected?


# In[12]:


nx.number_connected_components(marvel) # How many components are there?


# In[13]:


# Find the largest connected component (as a node set)
components = [G for G in nx.connected_components(marvel)]
largest = max(components, key=len)


# ## Centrality
# 
# Below I show just one example, but there are a range of [centrality functions](https://networkx.org/documentation/stable/reference/algorithms/centrality.html) in NetworkX.

# In[14]:


# Calculate betweenness centrality for every node
bc = nx.betweenness_centrality(marvel)


# In[15]:


# Add a node attribute from a centrality measure
nx.set_node_attributes(marvel,bc,"betweenness")


# In[16]:


# Create a dataframe of nodes
nodes = pd.DataFrame.from_dict(marvel.nodes, orient='index')
nodes.reset_index(level=0,names="character",inplace=True)
nodes


# In[17]:


# See the distribution for a metric
sns.displot(x="betweenness", binwidth=.005, data=nodes)


# ## Triangles and Clustering

# In[30]:


# Get number of triangles for every node
nx.triangles(marvel)

# n.b. Pay attention to the following note from the NetworkX docs:
# When computing triangles for the entire graph each triangle is counted three times, once at each node.


# In[20]:


# Get clustering coefficients
# These can be added to a node dataframe as above
nx.clustering(marvel)


# In[21]:


# Find the average clustering coefficient
nx.average_clustering(marvel)


# ## Bridges

# In[23]:


# List a network's bridges
list(nx.bridges(marvel))


# In[25]:


# Test if a network has any bridges
nx.has_bridges(marvel)


# In[27]:


# List a network's local bridges
list(nx.local_bridges(marvel))


# ## Neigbors

# In[29]:


# Find a nodes neighbors
list(nx.neighbors(marvel, 'Death'))


# In[32]:


# Find common neighbors of a node pair
list(nx.common_neighbors(marvel, 'Death', 'Zeus'))

