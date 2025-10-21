# Q22-8.py
# 8. pathlib을 사용하여 new_folder가 없으면 생성하세요.

from pathlib import Path


path = Path(r"C:\rokey\python\ch22\assingment22\new_folder")

if not path.is_dir():
    path.mkdir(exist_ok=True)