num = int(input())
ans = [0,1]
for i in range(num-1):
    next_num = ans[i] + ans[i+1]
    ans.append(next_num)
print(ans[num])