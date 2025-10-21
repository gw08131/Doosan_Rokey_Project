# pathlib_module.py

from pathlib import Path

# 현재 작업 디렉토리 확인
print(Path.cwd())

print("-----------")
# 2 경로 생성 및 조작
path = Path("C:/rokey/python/ch22/classify")
print(path/"file.txt")

print("-----------")
# 3 디렉토리 및 파일 존재 여부 확인
file = f"C:/rokey/python/ch22/classify/file.txt"
path = Path(file)
print(path.exists())        # 존재 여부 확인
print(path.is_file())       # 존재 및 파일 여부 확인
print(path.is_dir())        # 디렉토리 여부 확인

print("-----------")
# 디렉토리 생성 및 삭제
new_folder = "C:/rokey/python/ch22/classify/new_folder"
path = Path(new_folder)
path.mkdir(exist_ok=True)
path.rmdir()

print("-----------")
# 파일 생성 및 삭제
file = f"C:/rokey/python/ch22/classify/file.txt"
file_path = Path(file)
file_path.touch()           # 빈 파일 (용량이 0인)
file_path.unlink()          # 파일 삭제

print("-----------")
# 파일 및 폴더 목록 조회
dir = "C:/rokey/python/ch22/classify"
path = Path(dir)
for item in path.iterdir():
    print(item)         # 출력: C:\rokey\python\ch22\classify\pathlib_module.py

print("-----------")
# 파일 확장자 가져오기
file = f"C:/rokey/python/ch22/classify/file.txt"
path = Path(file)
print(path.suffix)          # 출력: .txt

print("-----------")
# 파일 이름 변경 및 이동하기
file = f"C:/rokey/python/ch22/classify"
path = Path(f"{file}/old_name.txt")
path.touch()        # 파일 생성
new_name = path.rename(f"{file}/new_name.txt")