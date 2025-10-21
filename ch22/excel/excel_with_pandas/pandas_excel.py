# pandas_excel.py

from openpyxl import workbook, load_workbook
import pandas as pd

# 엑셀 파일 읽기
path = r"C:\rokey\python\ch22\excel\sample.xlsx"
df = pd.read_excel(path,sheet_name="Sample Data")
print(df.head())

print("--------------")
# Excel 파일 정보 확인
df.info()               # 데이터 타입 및 개요 확인  
print(df.describe())    # 숫자 데이터 요약


print(df["나이"])
print(df["나이"].sum())
print(df["나이"].mean())

df["출생년도"] = 2025 - df['나이']
print(df.head())

print("--------------")
path = r"C:\rokey\python\ch22\excel\modified_sample.xlsx"
df.to_excel(path, index = False)        # index 제외하고 저장