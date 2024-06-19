import sys

input = sys.stdin.readline
input_num = int(input())
operand = []
ans = []

maximum = -1e9
minimum = 1e9

operand = list(map(int, input().split()))
operator = list(map(int, input().split()))

def back(depth, sum, plus, minus, multiply, divide):
    global maximum,minimum
    if depth == input_num: 
        ans.append(sum)
        maximum = max(sum,maximum)
        minimum = min(sum,minimum)
        return 
    if plus:
        back(depth+1,sum + operand[depth],plus-1, minus,multiply,divide)
    if minus:
        back(depth+1,sum - operand[depth],plus, minus-1,multiply,divide)
    if multiply:
        back(depth+1,sum * operand[depth],plus, minus,multiply-1,divide)    
    if divide:
        back(depth+1,int(sum /operand[depth]),plus, minus,multiply,divide-1) 
           
back(1,operand[0],operator[0],operator[1],operator[2],operator[3])
print(maximum)
print(minimum)