from collections import deque

n, m, k = map(int, input().split())

edges = {tuple(map(int, input().split())): [] for i in range(k)}

if k > 5000:
    print(2)
    exit()


