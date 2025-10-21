# 1_manageFile.py

# 특정 폴더에서 텍스트 파일만 찾아 복사/이동/삭제하는 프로그램


import os
import shutil

folder_path = r"C:\rokey\python\ch22\manage_file"


def list_test_files(folder_path):
    """
    1. 특정 폴더에서 모든 .txt 파일을 검색하여 
    리스트로 반환하는 함수를 작성
    """
    
    f_list = []
    files = os.listdir(folder_path)
    # print(files)
    for file in files:
        if file[-4:] == ".txt":
            f_list.append(file)

    return f_list

def copy_text_files(source_folder,destination_folder):
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    
    for file in list_test_files(source_folder):
        shutil.copy(os.path.join(source_folder,file),
                     os.path.join(destination_folder,file))
        print(f"파일 복사 완료: {file}")

if __name__ == "__main__":

    folder = f"C:/rokey/python/ch22/manage_file/folder1"
    if not os.path.exists(folder):
        os.mkdir(folder)

    file1 = f"{folder}/file1.txt"
    file2 = f"{folder}/file2.csv"
    with open(file1,'w') as f:
        f.write("file1\n")
    with open(file2,'w') as f:
        f.write("file2\n")    


    source = r"C:\rokey\python\ch22\manage_file\folder1"        # 원본 폴더
    print("txt 파일 목록: ",list_test_files(source))
    
    destination1 = r"C:\rokey\python\ch22\manage_file\folder2"
    copy_text_files(source,destination1)