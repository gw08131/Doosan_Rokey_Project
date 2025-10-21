#dfs.py

myGraph = {"A":["B","C","D"],
           "B":["A","E"],
           "C":["A","F","G"],
           "D":["A","H"],
           "E":["B","I"],
           "F":["C","J"],
           "G":["C"],
           "H":["D"],
           "I":["E"],
           "J":["F"]}

def my_dfs(graph, start_node):
    
    stack = list()      # 스텍 (빈 리스트) 생성

    visited = list()    # 방문 확인용 리스트 생성

    stack.append(start_node)        # 시작 노드 스텍에 push

    # stack 내용이 비면 while문 빠져나옴
    while stack:                # stack에 내용이 있으면 while문 계속 돌림
        node = stack.pop()      # 스텍에서 노드 꺼냄

        if node not in visited:     # 방문하지 않았다면..
            visited.append(node)    # 방문처리             
            # 인접 노드를 스택에 삽입
            stack.extend(reversed(graph[node]))           # "A":["B","C","D"] -> node = "A" 그래서 stack 저장에 B,C,D가 됨
    print(f"dfs = {visited}")        
    return visited  # 방문 순서 확인

my_dfs(myGraph,"A")
# print(my_dfs(myGraph,"A"))