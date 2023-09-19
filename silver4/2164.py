from collections import deque

N = int(input())
dq = deque(range(1, N+1))

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.popleft())


# deque를 사용하면 시간초과가 나지 않는다.
# deque는 양쪽에서 모두 append, pop이 가능하다.
# range로 값을 넣어줘야 시간초과가 나지 않는다. (for문으로 일일이 값을 넣어주면 시간초과남)
