import sys

input = sys.stdin.readline

total_num = int(input())

stack=[]
problem = list(map(int,input().split()))
answer = total_num* [-1]
for i in range(total_num):
    while stack and problem[stack[-1]]<problem[i]:
        answer[stack[-1]] = problem[i]
        stack.pop()
    stack.append(i) 
    
print(*answer)   
    
    
