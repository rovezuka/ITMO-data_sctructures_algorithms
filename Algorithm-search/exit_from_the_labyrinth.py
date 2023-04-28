import copy

lab = [
                [1 for i in range(15)],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1 for i in range(15)]
                ]


def gr(lab, n, m):
    sl = {}
    for j in range(m):
        for i in range(n):
            if lab[i][j] == 0:
                sl[(i,j)]= []
    for el in sl:
        if el[1]==0:
            if lab[el[0]][el[1]+1] == 0:
                sl[el] = sl[el] + [(el[0], el[1]+1)]
        elif el[1]==14:
            if lab[el[0]][el[1]-1] == 0:
                sl[el] = sl[el] + [(el[0], el[1]-1)]
        elif el[0]==0:
            if lab[el[0]+1][el[1]] == 0:
                sl[el] = sl[el] + [(el[0]+1, el[1])]
            if lab[el[0]][el[1]+1] == 0:
                sl[el] = sl[el] + [(el[0], el[1]+1)]
            if lab[el[0]][el[1]-1] == 0:
                sl[el] = sl[el] + [(el[0], el[1]-1)]
        elif el[0]==14:
            if lab[el[0]-1][el[1]] == 0:
                sl[el] = sl[el] + [(el[0]-1, el[1])]
            if lab[el[0]][el[1]+1] == 0:
                sl[el] = sl[el] + [(el[0], el[1]+1)]
            if lab[el[0]][el[1]-1] == 0:
                sl[el] = sl[el] + [(el[0], el[1]-1)]
        else:
            if lab[el[0]+1][el[1]] == 0:
                sl[el] = sl[el] + [(el[0]+1, el[1])]
            if lab[el[0]-1][el[1]] == 0:
                sl[el] = sl[el] + [(el[0]-1, el[1])]
            if lab[el[0]][el[1]+1] == 0:
                sl[el] = sl[el] + [(el[0], el[1]+1)]
            if lab[el[0]][el[1]-1] == 0:
                sl[el] = sl[el] + [(el[0], el[1]-1)]
    return sl


sl = gr(lab,15,15)
minim = float('inf')
route = []

def dfs(startP, searchP, graph, visited, k):
    global minim
    global route
    if startP == searchP:
        return k, route

    for neib in graph[startP]:
        if neib not in visited:
            visited.append(neib)
            m = dfs(neib, searchP, graph, visited, k+1)[0]
            if m < minim:
                minim = m
                route = copy.deepcopy(visited)
            visited.remove(neib)

    return minim, route

ot = dfs((7, 0), (7, 14) , sl, [(7, 0)], 1)

for i in ot[1]:
    lab[i[0]][i[1]] = '*'

print(f'Сделано шагов {ot[0]}')
print(f'Маршрут {ot[1]}')
for i in range(len(lab)):
    print(lab[i])