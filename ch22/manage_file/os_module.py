# os_module.py

import os

# (1) 현재 작업 디렉토리 확인
print(f"현재 작업 디렉터리: {os.getcwd()}")

# 작업 디렉토리 변경
os.chdir(r"C:\rokey\python\ch22\manage_file")

# 변경된 작업 디렉토리 확인
print(f"현재 작업 디렉터리: {os.getcwd()}")

# (2) 디렉토리 및 파일 목록 조회
print("-------------------")
print(f"디렉터리 목록: {os.listdir(".")}")

# (3) 디렉토리 생성 및 삭제
print("-------------------")
os.mkdir("test_dir")    # 디렉토리 생성
os.rmdir("test_dir")

if os.path.exists("file.txt"):
    print("파일이 존재합니다.")

# (5) 파일 및 디렉토리 경로 다루기
folder = os.getcwd()
print(os.path.join(folder,"file.txt"))          # 경로 합치기
print(os.path.basename(f"{folder}/file.txt"))   # 파일명만 추출
print(os.path.dirname(f"{folder}/file.txt"))   # 디렉토리 경로 추출
