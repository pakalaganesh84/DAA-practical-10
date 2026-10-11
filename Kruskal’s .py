def kruskal(edges, vertices):
    parent = list(range(vertices))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    mst = []
    edges.sort(key=lambda edge: edge[2])

    for u, v, weight in edges:
        root_u = find(u)
        root_v = find(v)

        if root_u != root_v:
            mst.append((u, v, weight))
            parent[root_u] = root_v

    print("Edges in Minimum Spanning Tree:")
    total = 0
    for u, v, weight in mst:
        print(u, "-", v, ":", weight)
        total += weight

    print("Total cost:", total)


edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

kruskal(edges, 4)
