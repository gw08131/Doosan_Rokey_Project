# Q23-10.py

# 10. logfile.log에서 2025-03-30 날짜의 로그만 추출하세요.
# 예제 로그 파일 생성 코드

import requests

path = r"ch23\assignmnet23\homework\logfile.log"
with open(path, "w", encoding="utf-8") as file:
    file.write("2025-03-30 12:00:01 INFO 서버 시작됨\n")
    file.write("2025-03-30 12:05:12 ERROR 데이터베이스 연결 실패\n")
    file.write("2025-03-30 12:10:35 WARNING 응답 속도 저하\n")
    file.write("2025-03-30 12:15:45 ERROR 사용자 인증 실패\n")

with open(path, "r", encoding="utf-8") as file:
    for line in file:
        if "2025-03-30" in line:
            print(line.strip())