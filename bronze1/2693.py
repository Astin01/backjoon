test_case = int(input())

for i in range(test_case):
    case = list(map(int,input().split()))
    case.sort(reverse=True)
    print(case[2])