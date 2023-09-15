for _ in range(int(input())):
    stk = []
    isVPS = True
    for ch in input():
        if ch == '(':
            stk.append(ch)

        else:
            if stk:
                stk.pop()
            else:
                isVPS = False
    if stk:
        isVPS = False
    if isVPS:
        print('YES')
    else:
        print('NO')


# t번 반복한다.

# 1번 실행 할 때 들어오는 input을 하나씩 분해해서
# (는 스택 안에 넣어준다.

# )가 들어온다면
# 스택안의 (를 꺼내준다
# 만약 (가 없다면 VPS가 아니므로 false를 반환한다.

# input을 반복해서 더 이상 아무것도 없다면 vps이므로 true를 반환
