import sys

input = sys.stdin.readline

input_num = int(input())

now_num = 1
stack = []
answer = []
flag = True
for _ in range(input_num):
    put_num = int(input())
    while(now_num<=put_num):
        stack.append(now_num)
        now_num+=1
        answer.append("+")
    
    if(stack[-1] == put_num):
        stack.pop()
        answer.append("-")
    else: 
        print("NO")
        flag = False
        break
if flag:
    for i in answer:
        print(i)
    
        