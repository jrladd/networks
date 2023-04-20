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
- **span**: the length of the path between two nodes if the local bridge between them were removed.
- **weak ties**: a low-weight edge that typically has high betweenness, acting as a bridge. Weak ties are often the casual social acquaintances that tie a social network together and allow information to flow between groups, as in Granovetter's famous article "The Strength of Weak Ties." 
- **strong triadic closure property**: if a node has two *strong* edges to two other nodes, this property says there should be either a strong or weak edge between them. This is a version of triadic closure that accounts for strong edges specifically.
- **neighborhood overlap**: for two nodes A and B, the number of nodes who are neighbors of *both* A and B divided by the total neighbors of A or B.
- **structural holes**: "the 'empty space' in the network between two sets of nodes that do not otherwise interact closely" (Easley & Kleinberg 67).
- **broker**: a node that can communicate between groups and across structural holes, often also a pivotal node.

## Homophily and Communities

- **homophily**: the network principle that describes the way that nodes which have common properties or attributes are likely to be or become linked to one another.
- **assortative mixing**: a synonym for homophily.
- **mixed edge**: an edge between nodes of different types or properties.
- **selection**: "the tendency of people to form friendships with others who are like them" (Easley and Kleinberg 90).
- **social influence**: the opposite of selection, i.e. the tendence of people to select their preferences and attributes based on their friendships.
- **community detection**: a set of methods to determine subgroups or communities within a network.
- **component**: a part of a network in which paths exist from any node to any other node.
- **clique**: a subset of nodes in a network in which every node is connected any other. Cliques can have any number of nodes, and a triangle is the simplest type of clique.
- **community**: a subset of nodes in a network, usually determined by some community detection method.
- **embeddedness**: the number of neighbors that two nodes have in common, i.e. the first part of the formula for neighborhood overlap.
- **partition**: a subset of nodes in a network, determined by a community detection method, a node attribute, or a completely different node type.
- **modularity**: a set of community detection methods that tries to determine communities based on their internal density. The Louvain method is a type of modularity.

## Special Network Types

- **signed network**: a network that has positive or negative edges. These positive or negative signs are often part of an edge's weight: 1 for a positive edge, -1 for a negative edge, 0 for no edge.
- **structural balance**: the network principle that describes how signed networks seek to become balanced by changing between positive and negative edges. In any set of three nodes, the set is structurally balanced if there are either three positive edges or just one.
- **directed networks**: a network in which edges are directed from a source to a target. For example, in a correspondence network with edges representing letters sent, those letters have a sender (source) and a recipient (target).
- **directed path**: a path in a network with the direction of edges going in the same direction. In a directed network, paths can only be traversed if they are appropriately directed. 
- **strongly connected components**: a component in which there is a *directed* path from every node to every other node. If there are paths between every node but not all of those paths are directed, then it is a weakly connected component.
- **in-degree**: the number of edges for which a given node is the target, i.e. the number of edges coming in.
- **out-degree**: the number of edges for which a given node is the source, i.e. the number of edges going out.
- **"bow-tie" structure**: a common directed network structure seen on the Web, in which a network has three large strongly connected components. One of these is a massive component in the center that has a slightly smaller component with edges only coming in and another smaller component with edges only going out.
- **bipartite network**: a network with two distinct node types or partitions. Often the two node types are an entity and a group, as in an affiliation network.
- **multipartite network**: a network with more than one distinct node types. Bipartite networks are type of multipartite networks.
- **incidence matrix/biadjacency matrix**: the bipartite version of the adjacency matrix, in which the rows represent nodes of on type and the columns represent nodes of the other type.
- **hypergraph**: another kind of network representing group affiliation, in which nodes are placed into groups rather than mapped to specific connections.
- **hyperedge**: the assignment to overlapping groups that occurs in a hypergraph. Hyperedges are usually visually represented as curving areas drawn around groups of nodes.
- **projection**: the process of turning a bipartite network into a unipartite network by turning one node set into the new network's nodes and the second node set into its edges.
- **multilayer network**: a network with more than type of edges, usually organized into "layers."
- **temporal/dynamic network**: a special kind of multilayer network showing change over time, in which the nodes are persistent but the edges change over time. A temporal network is a type of "multiplex" network, i.e. a multilayer network with nodes that persist across layers.
- **topological overlap**: the amount of agreement or similarity between edges across layers in a multilayer network, usually expressed as a value between 0 and 1. A network that stays relatively the same over time will have high topological overlap.

## Network Behavior

- **diffusion**: the way in which behaviors spread across a social network.
- **cascade**: a specific kind of diffusion in which a new behavior is iteratively triggered to "cascade" from node to node across a network.
- **complete cascade**: a cascade in which the new behavior spreads to every node in the network.
- **coordination game**: a system that describes how people make decisions to adopt new behaviors based on the payoff of those behaviors. If two people adopt the same behavior, they each get the payoff assigned to that behavior.
- **cascade threshold**: adapted from a simple coordination game, the threshold at which the ratio of a node's neighbors that have adopted a new behavior A will cause it to switch from old behavior B. If behavior A has a payoff a and B has a payoff b, then the value of the cascade threshold will be $\frac{b}{a+b}$.
- **cascade capacity**: "the largest threshold at which a finite set of nodes can cause a complete cascade" (Easley & Kleinberg 587).
- **bilingual option**: an additional option for a coordination game, in which an individual can adopt *both* behaviors instead of just one. Adopting both behaviors usually comes with an additional cost.
- $R_{0}$ **(R-zero or R-naught)**: the basic reproductive number. In a branching process epidemic, the amount of people it is possible for an individual to infect, equal to the probability of infection times the number of contacts.
- **SIR epidemic**: an epidemic with three states, susceptible (in which a person has the potential to become infected but is not yet infected), infections, and removed (in which a person has already been infected and can't be reinfected).
- **SIS epidemic**: an epidemic with just the susceptible and infectious states, in which a person becomes susceptible again as soon as they are no longer infectious and can't be removed.
- **SIRS epidemic**: an epidemic in which individuals pass through a removed state of "immunity" before becoming infectious again.
- **percolation**: a way of viewing the dynamic process of an epidemic statically, be pre-calculating all the probabilities that an edge will carry disease.
- **synchronization**: in a Small World network, the process by which waves of an epidemic form over time due to network properties.