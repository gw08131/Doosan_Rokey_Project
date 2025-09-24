subject = ['국어', '수학', '영어', '국사']
print(subject)

subject.insert(0,'컴퓨터')
print(subject)          #subject = ['컴퓨터', '국어', '수학', '영어', '국사']

#수학과 영어 사이에 '음악' 과목 추가

#슬라이싱
print(subject[2:4])         #리스트명[시작인덱스(start): 끝인덱스-1(end)]
subject.insert (3,'음악')
print(subject)

subject2 = ['컴퓨터', '국어', '수학', '음악', '영어', '국사']
subject.extend(['미술','체육'])
print(subject)

#['컴퓨터', '국어', '수학', '음악', '영어', '국사', '미술', ' 체육']
subject3 = ['도덕','음악']
subject.insert(0, subject3[1])          #['음악', '컴퓨터', '국어', '수학', '음악', '영어', ' 국사', '미술', '체육']
print(subject)
subject.insert(0, subject3[0])          #['도덕', '음악', '컴퓨터', '국어', '수학', '음악', '영어', ' 국사', '미술', '체육']
print(subject)
