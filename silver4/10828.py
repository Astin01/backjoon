import sys

input = sys.stdin.readline

input_num = input()
list = []

def command(command):
    if command[0] == "push":
        list.append(command[1])
    elif command[0]== "pop":
        if len(list) == 0:
            print(-1)
        else:
            print(list.pop())
    elif command[0]== "size":
        print(len(list))
    elif command[0] == "empty":
        if len(list) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])
            
for i in range(int(input_num)):
    command(input().split())
    
# import sys
# input=sys.stdin.readline

# n=int(input())
# stack=[]

# def push(p):
#     stack.append(p)

# def pop():
#     if len(stack)!=0:
#         print(stack.pop())
#     else:
#         print(-1)

# def size():
#     print(len(stack))

# def empty():
#     if len(stack)==0:
#         print(1)
#     else:
#         print(0)

# def top():
#     if len(stack)!=0:
#         print(stack[-1])
#     else:
#         print(-1)
    
# for i in range(n):
#     command=input().split()
#     if command[0]=='push':
#         push(command[1])
#     elif command[0]=='pop':
#         pop()
#     elif command[0]=='size':
#         size()
#     elif command[0]=='empty':
#         empty()
#     elif command[0]=='top':
#         top()