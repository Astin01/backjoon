import heapq
import sys

input = sys.stdin.readline
min_pq = []
max_pq = []

for _ in range(int(input())):
    x = int(input())

    if x > 0:
        heapq.heappush(min_pq, x)
    elif x < 0:
        heapq.heappush(max_pq, -x)
    else:
        if min_pq and max_pq:
            if min_pq[0] < abs(-max_pq[0]):
                print(min_pq[0])
                heapq.heappop(min_pq)
            else:
                print(-max_pq[0])
                heapq.heappop(max_pq)
        elif min_pq:
            print(min_pq[0])
            heapq.heappop(min_pq)
        elif max_pq:
            print(-max_pq[0])
            heapq.heappop(max_pq)
        else:
            print(0)

# min 과 max 가 모두 있을때
# min만 있을때
# max만 있을때
# 둘다 없을때
