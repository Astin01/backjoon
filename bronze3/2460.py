max_people = 0
now_people = 0
for i in range(10):
    train_out, train_in =map(int,input().split())
    now_people -=train_out
    now_people +=train_in # now_people = train_in - train_out
    if(now_people > max_people): # max(now_people,max_people)
        max_people = now_people 
print(max_people)