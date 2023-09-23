n, k = map(int, input().split())
coin = []  # 2~5, coins = [int(input()) for _ in range(n))]
ans = 0
for _ in range(n):
    coin.append(int(input()))

sorted_coin = sorted(coin, reverse=True)  # coins.reverse()

for coin in sorted_coin:     # if문 불필요
    ans += int(k/coin)       # ans += k//coin
    k %= coin

print(ans)
