# p1_bfs.py

graph1 = {1:[2,3,4],
          2:[1,5],
          3:[1,6],
          4:[1,6],
          5:[2,6],
          6:[3,4,5]}

def bfs1(graph,start_node):
    queue = list()
    visited = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])               # [1, 4, 6, 5, 2, 3]
            queue.extend(reversed(graph[node]))     # [1, 4, 3, 2, 6, 5]
    return visited

print(bfs1(graph1,1))