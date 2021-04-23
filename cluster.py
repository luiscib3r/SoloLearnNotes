import numpy as np
import sys

sys.stdin = open('cluster3.txt')


n = int(input())

x = np.array([0.0, 0.0])

y = np.array([2.0, 2.0])

x_cluster = []
y_cluster = []


def dist(x1, x2):
    return np.sqrt(((x1-x2)**2).sum()).round(2)


for _ in range(n):
    p = np.array([float(x) for x in input().split()])

    px = dist(p, x)

    py = dist(p, y)

    if py >= px:
        x_cluster.append(p)
    else:
        y_cluster.append(p)


if len(x_cluster) != 0:
    x = np.array(x_cluster).mean(axis=0)
else:
    x = None


if len(y_cluster) != 0:
    y = np.array(y_cluster).mean(axis=0)
else:
    y = None

if x is None:
    print(x)
else:
    print(x.round(2))

if y is None:
    print(y)
else:
    print(np.round(y, 2))
