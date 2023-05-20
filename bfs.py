graph = {
    "3": ["9","20"],
    "9": ["3"],
    "20": ["15","7"],
    "15":["20"],
    "7":["20"],
}
def bfs(graph, node):
    big_max = [[node]]
    small = []
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        item = queue.pop(0)
        # print(item, end=" ")

        for m in graph[item]:
            if m not in visited:
                small.append(m)
                visited.append(m)
                queue.append(m)
        if small:
            big_max.append(small)
        small = []


    return visited, big_max
print(bfs(graph, "3"))
