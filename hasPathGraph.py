def construct_graph(edges):
    graph = {}
    for item in edges:
        a,b = item
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    return graph
def dfs(graph, source, destination, visited):
    if source == destination:
        return True
    if source in visited:
        return False
    visited.append(source)
    for item in graph[source]:
        if(dfs(graph, item, destination, visited)):
            return True
    return False
def hasPath(n, edges, source, destination):
    graph = construct_graph(edges)
    visited = []
    return dfs(graph, source, destination,visited)
print(hasPath(3, [[0,1],[1,2],[2,0]], 0, 2))

