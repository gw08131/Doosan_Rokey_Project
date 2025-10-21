# p3_ice_cube_tray.py

tray = [
        [0,0,1,1,0],
        [0,0,0,1,1],
        [1,1,1,1,1],
        [0,0,0,0,0]
        ]


n = len(tray)           #행
m = len(tray[0])        #열        

print(n,m)


#graph,start_node
def ice_cube_tray(x, y):
        stack = list()
        start_node = (x,y)
        stack.append(start_node)


        # 스텍이 비워지면 얼음 하나 확인
        while stack:
                x,y = stack.pop()
                
                # 주어진 범위를 벗어나면 무시
                if x < 0 or x >= n or y < 0 or y>=m:      
                # 범위를 벗어나는 경우
                        continue

                # 현재 노드를 아직 방문하지 않았으면
                if tray[x][y] == 0:
                        # 방문처리
                        tray[x][y] = 1
                        # 인접 노드를 스텍에 추가
                        stack.append((x-1,y))     # 좌노드
                        stack.append((x+1,y))     # 우노드
                        stack.append((x,y-1))     # 하노드
                        stack.append((x,y+1))     # 상노드
                        print("이동 경로 확인 ----------------------")
                        print(f"stack = {stack}")            # 노드 좌표
                        for i in tray:
                                print(i)
        
        # 얼음의 확인 여부 반환
        return True

count = 0
for i in range(n):
    for j in range(m):
        if tray[i][j] == 0:
            if ice_cube_tray(i, j) == True:
                count += 1
print(count)



