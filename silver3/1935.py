import sys

input = sys.stdin.readline

input_num = int(input())

input_string = input().rstrip()
number=[]
stack=[]
def calculator(str,stack):
    last = stack.pop()
    first = stack.pop()
    if(str == "+"):
         first = first + last # first +=last
    elif(str == "-"):
        first = first - last
    elif(str == "*"):
        first = first * last
    else:
        first = first / last
    stack.append(first)

for i in range(input_num):
    number.append(int(input())) # number=[int(input()) for i in range(N)]
    
for str in input_string:
    if(str.isalpha()):
        stack.append(number[ord(str)-65])
    else:
        calculator(str,stack)
        
print(f"{stack.pop():.2f}")