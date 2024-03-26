import sys

input = sys.stdin.readline

input_string = input().rstrip()
stack = []
ans=0

for i in range(len(input_string)):
    if(input_string[i] == "("):
        stack.append("(")
    else:
        if(input_string[i-1] == "("):
            stack.pop()
            ans+=len(stack)
        else:
            stack.pop()
            ans+=1
print(ans)      