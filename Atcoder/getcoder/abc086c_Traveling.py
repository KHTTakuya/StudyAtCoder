"""
2
3 1 2
6 1 1

Yes

https://atcoder.jp/contests/abs/tasks/arc089_a
"""

N = int(input())

# 初期位置t,x.yをしていする。
start = [0, 0, 0]
for _ in range(N):
    t, x, y = map(int, input().split())
    # のこり何秒なのかの確認
    dt = t - start[0]
    # 残りの距離数を絶対値で確認する。
    d = abs(x - start[1]) + abs(y - start[2])
    # 時間が距離より小さく、偶数になっているのかの確認
    if d <= dt and (dt - d) % 2 == 0:
        start = [t, x, y]
    else:
        print("No")
        break
else:
    print("Yes")
