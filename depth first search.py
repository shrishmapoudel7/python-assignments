# This function adds a new node to the graph.
#define add node

def add_node(node):
    if node not in graph:
        graph[node] = []



#This function adds an undirected edge between two nodes in the graph.
#define edge
        
def add_edge(node1, node2):
    if node1 in graph and node2 in graph:
        graph[node1].append(node2)     #  can traverse from node1 to node2 or from node2 to node1.
        graph[node2].append(node1)



#main section

def DFS(node, visited, graph):
    if node not in graph:
        print("Node is not present")
        return
    
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            DFS(neighbor, visited, graph)




# Global definitions
visited = set()
graph = {}

# Adding nodes
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

# Adding edges
add_edge("A", "B")
add_edge("B", "E")
add_edge("A", "C")
add_edge("A", "D")
add_edge("B", "D")
add_edge("C", "D")
add_edge("E", "D")

print(graph)

# Calling DFS
DFS("C", visited, graph)
