# assignmnet17.py

print("-----------6번-----------")

grid = [
        [0,1,1,1,1,1],
        [0,1,0,0,0,1],
        [0,1,0,1,0,1],
        [0,1,0,1,0,0],
        [0,0,0,1,1,0],
        [1,1,1,1,1,0]
        ]


print("-----------7번-----------")

grid = [
        [0,1,1,1,1,1],
        [0,1,0,0,0,1],
        [0,1,0,1,0,1],
        [0,1,0,1,0,0],
        [0,0,0,1,1,0],
        [1,1,1,1,1,0]
        ]

for i in range(len(grid)):
    print(grid[i])


print("-----------8번-----------")


# row = int(input("행:"))
# column = int(input("열:"))

# grid_list = []

# for i in range(row):
#     while True:
#             line_str = input("0과 1 입력: ")   # "0 1 0 1"
#             line_split = line_str.split(" ")      # ['0', '1', '0', '1']

#             if len(line_split) != column:
#                 print(f"입력 개수가 {len(line_split)}개입니다. {column}개를 입력해야 합니다.")
#                 continue
            
#             else:
#                 line_int = list(map(int, line_split))  # [0, 1, 0, 1]
#                 grid_list.append(line_int)
#                 break


# print(grid_list)



print("\n-----------9번-----------")


stack = []
visited = []

n = len(grid)
m = len(grid[0])

def dfs_map(graph, start_node):
    stack.append(start_node)

    while stack:
        x, y = stack.pop()

        # 지도 범위 벗어나면 무시
        if x < 0 or x >= n or y < 0 or y >= m:
            continue

        # 이미 방문했거나 벽(1)이면 패스
        if (x, y) in visited or graph[x][y] == 1:
            continue

        # 방문 처리
        visited.append((x, y))

        # 인접 노드 탐색
        stack.append((x - 1, y))
        stack.append((x + 1, y))
        stack.append((x, y - 1))
        stack.append((x, y + 1))
    
    return True

count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and (i, j) not in visited:
            if dfs_map(grid, (i, j)) == True:
                count += 1
print(count)


print("\n-----------10번-----------")

grid = [
        [0,1,1,1,1,1],
        [0,1,0,0,0,1],
        [0,1,0,1,0,1],
        [0,1,0,1,0,0],
        [0,0,0,1,1,0],
        [1,1,1,1,1,0]
        ]

n = len(grid)
m = len(grid[0])

queue = []
visited = []

def bfs_map(graph, start_node):
    queue.append(start_node)

    while queue:
        x, y = queue.pop(0)

        # 범위 벗어나면 무시
        if x < 0 or x >= n or y < 0 or y >= m:
            continue

        # 아직 방문 안했고, 0인 길이라면
        if (x, y) not in visited and graph[x][y] == 0:
            visited.append((x, y))  # 좌표 저장!

            # 인접 노드 추가
            queue.append((x+1, y))
            queue.append((x-1, y))
            queue.append((x, y+1))
            queue.append((x, y-1))

    return True

count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and (i, j) not in visited:  # 방문 여부 확인
            if bfs_map(grid, (i, j)):
                count += 1

print(count)
