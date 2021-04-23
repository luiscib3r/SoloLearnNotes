import sys

import numpy as np

sys.stdin = open('reshape_input.txt')

r = int(input()) 
lst = [float(x) for x in input().split()]
arr = np.array(lst)

print(arr.reshape(r, int(arr.shape[0]/r)))