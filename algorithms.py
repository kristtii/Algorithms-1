def dfs(graph):
    connected_components = 0
    connected_component_array = [0] * graph.size()
    visited = [False] * graph.size()


    for node in graph.nodes():
        if(not visited[node.value()]):
            explore(graph, node, visited, connected_component_array, connected_components):
            connected_components += 1
    
    return connected_component_array

def explore(graph, node, visited, connected_component_array, connected_components):
    current_node = node

    visited[current_node.value()] = True
    connected_component_array[current_node.value()] = connected_components

    while current_node.next != None:
        if not visited[current_node.next.value]:
            explore(graph, graph.nodes[current_node.next.value], visited, connected_component_array, connected_components)
        current_node = current_node.next

def calculate_pairings(n, connected_components_array):
    
    graphsize = connected_components_array.size

    connected_components_vertices = [0] * graphsize
    for i in range(graphsize):
        connected_components_vertices[connected_components_array[i]] += 1

    pairings = 0
    for i in range(graphsize):
        n -= connected_components_vertices[i]
        if(n == 0):
            break
        pairings += n * connected_components_vertices[i]

    return pairings



