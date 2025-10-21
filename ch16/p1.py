# p1.py

# 문제 1: 괄호 짝 검사

# 입력: 문자열
# 반환: True (짝 맞음), False (짝 안맞음)

# 1. 빈 스텍을 생성
# 2. 표현식 내 문자를 가져와 (반복)
# 3. 만약 문자에 "시작하는" 괄호가 있다면 스텍에 push
# 4. "끝나는" 괄호가 있다면 스텍에서 pop
#     4-1. 만약 스텍이 비어있다면 False
#     4-2.  pop한 괄호를 확인하여 모두 서로 일치하지 않으면 False
# 5. 스텍이 비어있다면 True


test_text = "[1+{(a+b)}]"

def check_brackets(text):
    brackets = []
    count = 0
    for ch in text:
        count += 1
        if ch in "({[":
            brackets.append(ch)
            print(f"{count}: stack에 괄호 넣기 = {brackets}")

        elif ch in ")}]":
            if not brackets:                # 시작 괄호가 있는지 없는지 확인
                print(f"{count}: ❌ 시작 괄호가 없음. 현재 문자: {ch}")
                return False
            top = brackets[-1]            #pop 된 value?가 top인건가?

            if ch ==")" and top == "("or \
                ch =="}" and top =="{" or \
                ch =="]" and top =="[":
                brackets.pop()
                print(f"{count}: ✅ 괄호 짝 맞음. pop 이후 = {brackets}")

            else:
                print(f"{count}: ❌ 짝이 안 맞음! 현재 문자: {ch}, 스택 top: {top}")
                return False
            
    if brackets:
        print(f"❗ 남아 있는 스택: {brackets}")        
    return len(brackets) == 0       # True
    # len(brackets) → 스택에 남아 있는 괄호 개수
            

print(check_brackets(test_text))
