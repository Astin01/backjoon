booklist = {}  # booklist = dict() 도 가능
for _ in range(int(input())):
    book = input()
    if book in booklist:
        booklist[book] += 1
    else:
        booklist[book] = 1
m = max(booklist.values())
max_list = []
for key, value in booklist.items():
    if value == m:
        max_list.append(key)
max_list.sort()
print(max_list[0])

# 최댓값이 동일한 요소가 여러개인 경우를 대비해서
# 최댓값이 같은 값들을 list에 모으고
# 사전순으로 출력하기 위해 sort 해준다.
