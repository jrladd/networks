# Key Terms and Definitions

## Basic Terms

- **graph/network**: a system of connections, composed of nodes an edges
- **node**: any entity included in a network, the thing being connected, also known as a vertex or an actor. Nodes are often represented as circles in network visualizations.
- **edge**: any relationship, also known as a link or a tie, that connects two nodes. Edges are often represented as lines in network visualizations.
- **scale-free network**: a network in which the distribution of connections is the same in small areas of the network as it is in the entire thing.
- **small world network**: a common kind of network with a large number of very low-degree nodes and a small number of very high-degree ones. A small world network high density and low average path length. 
- **Six Degrees of Separation**: In a small world network, it’s easy to get from one node to any other in 6 or 7 “steps” or “degrees” (i.e. path length). This kind of network very often describes networks of human relationships, and the small world phenomenon is most famously described in the “Six Degrees of Kevin Bacon” parlor game.
- **edge list**: a representation of a network as a list of source and target node pairs. Each row represents a single edge, and this information is often stored in a CSV or plaintext file.
- **adjacency list**: a representation of a network as a list of every node with all the nodes it is connected to.
- **adjacency matrix**: a representation of a network with every node as both columns and rows. The values in an adjacency matrix are numbers (most of 0s and 1s) representing the presence, absence, or weight of an edge.
- **neighbors**: the nodes directly connected to (i.e. adjacent to) a particular node.
- **isolates**: nodes with no connections and therefore no neighbors.
- **hub**: a node with many connections to other nodes. Hubs are common in small world networks.

## Types of Networks

- **communication network**: a network in which edges represent communication between entities. A network of letter-writing is a communication network.
- **social network**: a network in which edges represent social relationships, as in familial or friendship networks.
- **information network (information linkage)**: a network in which edges represent connections between pieces of information, like hyperlinks on the web.
- **collaboration network**: a network in which edges represent collaborative work between two nodes, as in a copublication network.
- **technological network**: a network in which the nodes and edges are pieces of technology, like local computer networks or the Internet.
- **who-talks-to-whom network**: a network in which edges represent communication between people, a subset of communication networks.
- **affiliation network**: a bipartite network in which edges represent group affiliation.
- **networks in the natural world**: a network in which the nodes and edges are part of the natural world, i.e. ecological networks, fungal networks, neural networks.
- **citation network**: a directed network in which edges represent citations.
- **semantic network**: a network in which edges represent relationships between words, often directed.

## Paths and Metrics

- **path**: a series of edges that connects two nodes that do not have a direct edge between them. Nodes three steps away from each other in a network have a path length of 3.
- **cycle**: a path that returns back to the original node, forming a "circle" of edges.
- **connected graph**: a network made up of a single connected component. Many networks are not connected.
- **component (connected component)**: a part of a network in which paths exist from any node to any other node.
- **giant component**: a large component comprising most of the nodes in a network. Many networks wind up with a single giant component and several smaller components.
- **path length**: the number of edges making up a path.
- **distance (shortest path length)**: the number of edges making up the shortest possible route between two nodes.
- **diameter**: the longest shortest path length in a component, often used to gauge the "width" of a network.
- **density**: the number of edges in the network divided by the total number of *possible* edges in the network, if every node were connected to every other node. Density tells us how connected a particular network is.
- **average distance**: the average of all shortest path lengths in the network; another common metric to describe a network's size.
- **pivotal node**: a node that lies on every shortest path between two other nodes.
- **breadth-first search**: a technique for searching a network "outward from a starting node, reaching the closest nodes first" (Easley & Kleinberg 34).
- **gatekeeper**: a nodes that lies on *every* path between two other nodes.
- **local gatekeeper**: a node with two neighbors that are not otherwise connected.

## Centrality

- **degree**: the number of connections or edges that a node has.
- **degree centrality**: the number of connections or edges that a node has, normalized against the size of the network.
- **strength**: the sum of the weights of all a node's connected edges.
- **betweenness centrality**: in its simplest form, the number of shortest paths that must pass through a particular node. Betweenness centrality helps to measure how often any path in the network must go through a node and therefore can show if a node is connected to many disparate groups in the network.
- **eigenvector centrality**: a centrality measurement based on a node’s degree and the degree of its immediate neighbors. A node can have high eigenvector centrality if it is adjacent to a high-degree node, even if the node itself doesn’t have very high degree. 
- **closeness centrality**: the reciprocal of the average shortest path length from a given node to all other nodes in the graph (or in the component, if the graph is not connected). In NetworkX, higher closeness centrality values indicate a more central node, but this is sometimes calculated so that the opposite is true.

## Visualization

- **tabular representation**: a network visualization that uses a table, like the edge table described above.
- **matrix visualization**: a visualization of a network's adjacency matrix, in which cell values are often replaced by colors.
- **node-link diagram**: the most common kind of network visualization, in which nodes are represented by circles and links or edges are represented by lines connecting them.
	- **irregular**: a node-link diagram layout in which nodes can be placed anywhere. A force-directed layout is a type of irregular layout.
	- **regular**: a layout in which nodes are placed hierarchically, as in a tree diagram.
	- **circular**: a layout in which nodes are placed in a circle or in concentric circles.
	- **rectilinear**: a layout in which nodes are placed on a line, usually to show some kind of change over time or other interval.
	- **parallel**: a layout in which two lines of nodes are placed side-by-side, usually used for bipartite networks and sometimes called a bipartite layout.
- **dynamic visualizations**: in contrast to static visualizations, visualizations that the viewer can interact with, usually made using web technologies.

## Clustering

- **triangles**: a set of three nodes where each node is connected to every other.
- **triadic closure**: the network phenomenon in which two unconnected nodes with a mutual neighbor will become connected.
- **clustering coefficient**: the ratio of how many of a node’s neighbors are connected to each other, relative to the total number of neighbors.
- **bridge**: an edge that, if removed, would cause a single component to split into two components.
- **local bridges**: an edge between two nodes that have no neighbors in common. If removed, it would make the path length between the two nodes increase by more than two.
- **span**: The length of the path between two nodes if the local bridge between them were removed.
- **weak ties**:
- **strong triadic closure property
- **neighborhood overlap
- **structural holes
- **brokers

## Homophily and Communities

- **homophily
- **assortative mixing
- **mixed edge
- **selection
- **social influence
- **community detection
- **component
- **clique
- **community
- **embeddedness
- **partition
- **modularity

## Special Network Types

- **signed networks
- **structural balance
- **directed networks
- **directed paths
- **strongly connected components
- **in-degree
- **out-degree
- **"bow-tie" structure
- **bipartite network
- **multipartite network
- **incidence matrix/biadjacency matrix
- **hypergraph
- **hyperedge
- **projection
- **multilayer network
- **temporal/dynamic network
- **topological overlap

## Network Behavior

- **diffusion
- **cascade
- **complete cascade
- **coordination game
- **cascade threshold
- **cascade capacity
- **bilingual option