import sys
from collections import deque

input = sys.stdin.readline

command_num = int(input())
deq = deque()

for _ in range(command_num):
    command = input().split()
    
    if command[0] == 'push':
        deq.append(command[1])
    elif command[0] == 'pop':
        if(len(deq) == 0):
            print(-1)
        else:
            print(deq.popleft())
    elif command[0] == 'front':
        if(len(deq) == 0):
            print(-1)
        else:
            print(deq[0])
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if(len(deq)==0):
            print(1)
        else:
            print(0)
    elif command[0] == 'back':
        if(len(deq) == 0):
            print(-1)
        else:
            print(deq[-1])
            
            
        
    