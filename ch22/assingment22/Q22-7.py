# Q22-7.py
# 7. pathlib을 사용하여 특정 폴더 내에서 .txt 확장자를 가진 파일 목록을 출력하세요.

from pathlib import Path

path = Path(r"C:\rokey\python\ch22\assingment22\sample_folder")

for item in path.iterdir():
    if item.suffix == ".txt":
        print(item.name)