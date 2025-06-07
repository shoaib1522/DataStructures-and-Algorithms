def undirected(vertices, edges, edge_list):
    graph=[]
    for i in range(vertices):
        graph.append([])
    for e in edge_list:
        s,d = e
        graph[s].append(d)
        graph[d].append(s) 
    for i in range(vertices):
        print(f"{i}-", end="")
        if len(graph[i]) == 0:
            print("Null")
        else:
            for j in range(len(graph[i])):
                if j == len(graph[i]) - 1:
                    print(f" {graph[i][j]}")
                else:
                    print(f" {graph[i][j]}",end="")
vertices=9
edges=8
edge_list = [
    (2, 0), (0, 3), (5, 2), (4, 6),
    (4, 0), (1, 3), (2, 1), (6, 1)
]
undirected(vertices, edges, edge_list)
