import sys

input = sys.stdin.readline
SMALL_ALPHABET_ASCII = 97
list = [0]*26
input_string = input().rstrip()

for char in input_string:
    list[ord(char)-SMALL_ALPHABET_ASCII] += 1
print(*list)