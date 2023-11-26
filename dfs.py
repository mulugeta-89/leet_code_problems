graph = {
    # 'A': ['B', 'C'],
    # 'B': ['A', 'D', 'E'],
    # 'C': ['A', 'F', 'G'],
    # 'D': ['B'],
    # 'E': ['B', 'F'],
    # 'F': ['C', 'E'],
    # 'G': ['C']
    "A" : ["B", "C"],
    "B" : ["A", "C"],
    "C": ["A", "B"]

}
def dfs(graph, start):
    visited = []
    stack = []
    stack.append(start)
    visited.append(start)
    result = []
    while stack:
        item = stack.pop()
        result.append(item)
        for neighbor in graph[item]:
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor)
    return result
def bfs(graph, start):
    queue = []
    visited = []
    visited.append(start)
    queue.append(start)
    while queue:
        item = queue.pop(0)
        print(item)
        for neighbor in graph[item]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
visited = []
def dfsRecur(graph, start, visited):
    if start in visited:
        return False
    visited.append(start)
    for neighbor in graph[start]:
        dfsRecur(graph, neighbor, visited)
    return True
def connectedComponent(graph):
    count = 0
    for node in graph:
        if dfsRecur(graph, node, visited):
            count += 1
    return count
def largestConnectedComponent(graph):
    maxi = -float("inf")
    for node in graph:
        size = dfsi(graph, node, visited)
        maxi = max(maxi, size)
    return maxi

def dfsi(graph, start, visited):
    if start in visited:
        return 0
    visited.append(start)
    count = 1
    for neighbor in graph[start]:
        count += dfsi(graph, neighbor, visited)
    return count
def shortestPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    queue = [[nodeA, 0]]
    visited = [nodeA]
    while queue:
        node, distance = queue.pop()
        if node == nodeB:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append([neighbor, distance+1])
    return -1
def numberOfIslands(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                count += 1
    return count
def explore(grid, r,c, visited):
    rowInbounds = r >= 0 and r < len(grid)
    colInbounds = c >= 0 and c < len(grid[0])
    if not rowInbounds or  not colInbounds or grid[r][c] == "0":
        return False
    position = str(r) + "," + str(c)
    if position in visited:
        return False
    visited.add(position)
    explore(grid, r-1, c, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c-1, visited)
    explore(grid, r, c+1, visited)
    return True
def minimumIsland(grid):
    mini = float("inf")
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = dfsCount(grid, r, c, visited)
            if size > 0:
                mini = min(mini, size)
    return mini
def dfsCount(grid, r, c, visited):
    rowInBound = r >= 0 and r < len(grid)
    colInBound = c >= 0 and c < len(grid[0])
    if not rowInBound or not colInBound or grid[r][c] == "W"or (r,c) in visited:
        return 0
    visited.add((r,c))
    count = 1
    count += dfsCount(grid, r-1, c, visited)
    count += dfsCount(grid, r+1, c, visited)
    count += dfsCount(grid, r, c-1, visited)
    count += dfsCount(grid, r, c+1, visited)
    return count
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
print(minimumIsland(grid))

def buildGraph(edges):
    graph = {}
    for item in edges:
        a,b = item
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph
edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

