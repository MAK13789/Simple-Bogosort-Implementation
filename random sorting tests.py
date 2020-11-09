def is_sort(y):
    for i in range(len(y) - 1):
        if y[i] > y[i+1]:
            return False
    return True
import numpy as np
def slow_sort(x):
    temp = np.random.permutation(x)
    while (is_sort(temp) == False):
        temp = np.random.permutation(x)
    return temp
def gen_rand(n):
    return (list(np.random.permutation([j for j in range(1, n)])))
slow_sort(gen_rand(15))