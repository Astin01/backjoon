import sys
from collections import deque

input = sys.stdin.readline
problem = deque()
answer = deque()

def set_deq(num):
    for i in range(num):
        problem.append(i+1)

input_num = input().split()

set_deq(int(input_num[0]))

while(len(problem)):
    problem.rotate(-int(input_num[1]))
    answer.append(problem.pop())


print("<" + ", ".join(map(str,answer)) + ">")