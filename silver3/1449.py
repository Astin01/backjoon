N, L = map(int, input().split())
coord = [False]*1001
ans = 0
j = 0
for i in map(int, input().split()):
    coord[i] = True

while j < 1001:
    if coord[j]:
        ans += 1
        j += L
    else:
        j += 1

print(ans)
