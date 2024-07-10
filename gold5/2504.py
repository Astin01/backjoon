bracket = input()
stack = []
calc = 1
ans=0
for i in range(len(bracket)):
    if bracket[i] == "(":
        stack.append(bracket[i])
        calc*=2
    elif bracket[i] == "[":
        stack.append(bracket[i])
        calc*=3
    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            ans=0
            break
        if bracket[i-1]=="(":
            ans += calc   
        stack.pop()
        calc//=2  
    else:
        if not stack or stack[-1] == "(":
            ans=0
            break
        if bracket[i-1] =='[':
            ans+=calc
        stack.pop()
        calc //=3 

if stack:
    print(0)
else:
    print(ans)
        
        