import copy

graph = { 'A': ['B', 'C'],
          'B': ['A', 'D'],
          'C': ['A', 'D', 'F', 'E'],
          'D': ['B', 'C'],
          'E': ['C', 'F', 'G'],
          'F': ['C', 'E', 'G'],
          'G': ['E', 'F', 'H', 'K'],
          'H': ['G', 'K'],
          'K': ['G', 'H']
}

maxim = 0
route = []

def dfs(startP, searchP, graph, visited, k):
    global maxim
    global route
    if startP == searchP:
        return k, route

    for neib in graph[startP]:
        if neib not in visited:
            visited.append(neib)
            m = dfs(neib, searchP, graph, visited, k+1)[0]
            if m > maxim:
                maxim = m
                route = copy.deepcopy(visited)
            visited.remove(neib)

    return maxim, route

print(dfs('A', 'K', graph, ['A'], 0))