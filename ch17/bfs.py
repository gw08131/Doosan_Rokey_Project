# bfs.py

from graph import myGraph

def my_bfs(graph,start_node):
    queue = list()
    visited = list()

    queue.append(start_node)            # enqueue

    while queue:                        # queue의 내용이 없어질때까지 계속 반복
        node = queue.pop(0)

        if node not in visited:
            queue.extend(graph[node])       # 인접 노드를 가져다가 queue에다가 다 저장
            visited.append(node)
    print(f"bfs = {visited}")
    return visited

my_bfs(myGraph, "A")
#print(my_bfs(myGraph, "A"))