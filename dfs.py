graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'D': ['F'],
    'C': ['G', 'H'],
}
visiti = []
def dfs(graph, node, visiti):
    visiti.append(node)
    if node in graph:
        for item in graph[node]:
            if item not in visiti:
                dfs(graph, item, visiti)
    return visiti
print(dfs(graph, "A", visiti))
