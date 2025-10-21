# p1_dfs1.py

graph1 = {1:[2,3,4],
          2:[1,5],
          3:[1,6],
          4:[1,6],
          5:[2,6],
          6:[3,4,5]}

stack = list()
visited = list()

def dfs1(graph,start_node):

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited

print(dfs1(graph1,1))

