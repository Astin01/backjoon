import sys

input = sys.stdin.readline

input_num = input()

for _ in range(int(input_num)):
    string_list = input().split()
    for word in string_list:
        print(word[::-1], end=" ")
    print()
    
# n = int(input())

# for i in range(n):
# 	string = input()
# 	string += " "
# 	stack = []
#         for j in string:
#             if j != " ":
#                 stack.append(i)
#             else:
#                 while stack:
#                     print(stack.pop(), end="")
#                 print(' ', end='')