from itertools import combinations

height = []
for _ in range(9):
    n = int(input())
    height.append(n)  # 3~6, height = [int(input()) for _ in range(9)] 로 축약 가능

for i in combinations(height, 7):
    sum = 0
    for j in i:
        sum += j  # 9~11, sum(i)로 축약 가능
    if (sum == 100):
        sorted_height = (sorted(i))
        print(*sorted_height, sep='\n')
        exit()

# for combi in combinations(height,7):
#     if sum(combi) == 100:
#         for height in sorted(combi):
#             print(height)

#         break
#  이렇게도 가능
