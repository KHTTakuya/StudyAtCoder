"""
https://atcoder.jp/contests/abc234/tasks/abc234_d
"""

import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))
que = P[0:K]
print(min(que))
heapq.heapify(que)
for i in range(K, N):
    minima = heapq.heappop(que)
    minima = max(minima, P[i])
    heapq.heappush(que, minima)
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que, ans)