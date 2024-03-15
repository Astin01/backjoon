import sys

input = sys.stdin.readline

def set_editor(input_command):
    for i in input_command:
        left_stack.append(i)

def check_invalid(input_command):
    if(input_command == "L" and len(left_stack)==0):
        return True
    if(input_command == "D" and len(right_stack)==0):
        return True
    if(input_command == "B" and len(left_stack)==0):
        return True
        
def editor(input_command):
    if(check_invalid(input_command)):
        return
    if(input_command == "L"): # input_command[0] == "L" and left_stack
        popped = left_stack.pop()
        right_stack.append(popped) #right_stack.append(left_stack.pop())
    elif(input_command == "D"):
        popped = right_stack.pop()
        left_stack.append(popped)
    elif(input_command == "B"):
        left_stack.pop()
    else:
        command, input_word = input_command.split()
        left_stack.append(input_word) # left_stack.append(input_command[1])

def print_editor():
    if(len(left_stack)):
        for i in left_stack:
            print(i,end="")
    if(len(right_stack)):
        right_stack.reverse()
        for i in right_stack:# answer left_stack +right_stack[::-1]
            print(i,end="")  # print(''.join(answer))
        
init_string = input().rstrip()
command_count = int(input())
left_stack = []  # left = list(input())
right_stack = []
set_editor(init_string)

for _ in range(command_count):
    input_command = input().rstrip() # input().split()
    editor(input_command)
    
print_editor()
