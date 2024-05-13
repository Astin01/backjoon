import sys

input = sys.stdin.readline

input_string = list[input()]
answer = ""
stack = []

for str in input_string:
    if(str.isalpha()):
        answer+=str
