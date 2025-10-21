# 2_manageFile.py
# 특정 폴더 내의 파일을 확장자별로 자동 분류하는 프로그램


from pathlib import Path

def get_files(folder_path):
    """
    1. pathlib를 사용하여 특정 폴더 내의 
    모든 파일 목록을 반환하는 함수를 작성하시오.
    param: 검색할 폴더 경로 (folder_path)
    return: 파일 리스트
    """

    f_list = []
    folder = Path(folder_path)

    # for file in folder.iterdir():
    #     # print(file)
    #     if file.is_file() == True:
    #         f_list.append(str(file))

    # return f_list
    return [file for file in folder.iterdir() if file.is_file()]        # 컴프리헨션으로 쓰기

def organize_file_by_extension(source_folder):
    """
    2. 특정 폴더 내의 파일을 확장자 별로 
    폴더를 생성하여 이동하는 함수를 작성하시오.
    param: 정리할 폴더 경로 (source_folder)
    """
    source = Path(source_folder)
    if not source.exists():
        print("파일이 존재하지 않음")
        return

    # 특정 폴더의 파일 가져오기 
    for file in get_files(source):
        # 확장자 체크
        extension = file.suffix[1:]
        print(extension)

        # 확장자 이름 디렉터리 생성
        ext_folder = source/extension
        ext_folder.mkdir(exist_ok=True)

        # 확장자 이름 디렉터리에 파일 이동
        file.rename(ext_folder/file.name)           #file의 이름만 추출

        print(f"파일 이동 완료: {file.name}->{ext_folder}")

    return

if __name__ == "__main__":
    source = r"C:\rokey\python\ch22\classify\files"
    print("1. 파일 목록")
    print(get_files(source))
    print("2. 파일을 확장자별로 정리중...")
    organize_file_by_extension(source)