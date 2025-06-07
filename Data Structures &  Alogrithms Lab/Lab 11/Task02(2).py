def create_directed_graph(vertices, edges, edge_list):
    graph=[]
    for i in range(vertices):
        graph.append([])
    for e in edge_list:
        s, d = e
        graph[s].append(d) 
    for i in range(vertices):
        print(f"{i}->", end="")
        if len(graph[i]) == 0:
            print("Null")
        else:
            for j in range(len(graph[i])):
                if j == len(graph[i]) - 1:
                    print(f" {graph[i][j]}")
                else:
                    print(f" {graph[i][j]}", end="")
vertices = 8
edges = 11
edge_list = [
    (0, 3), (5, 7), (7, 5), (4, 6),
    (4, 2), (4, 7), (2, 5), (1, 5),
    (1, 6), (5, 6), (6, 5)
]
create_directed_graph(vertices, edges, edge_list)
