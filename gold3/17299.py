import sys
from collections import Counter

input = sys.stdin.readline

array_num = int(input())

stack=[]
problem=list(map(int,input().split()))
frequency=Counter(problem)
answer=[-1] * array_num

for i in range(array_num):
    while stack and frequency[problem[stack[-1]]]<frequency[problem[i]]:
        answer[stack.pop()] = problem[i]
    stack.append(i)
print(*answer)
