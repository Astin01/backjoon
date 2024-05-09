def conv_bi(n):
    ans = []
    while (n /2 !=0):
        remainder = n%2
        ans.append(remainder)
        n = n//2
    return ans;

def print_ans(ans):
    for i,value in enumerate(ans):
        if(value == 1):
            print(i,end=" ")
    print()
    
t = int(input())
    
for i in range(t):
    n = int(input())
    ans = conv_bi(n)
    print_ans(ans)
  
