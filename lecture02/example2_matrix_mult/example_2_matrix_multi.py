import numpy as np
import time
from numpy import random


def mult_nxn(n: int):

    A = [[random.rand() for _ in range(n)] for _ in range(n)]
    B = [[random.rand() for _ in range(n)] for _ in range(n)]
    C = [[0]*n]*n

    # Matrix multiplication using Python lists
    start_time = time.time()
    
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return time.time() - start_time


def numpy_nxn(n: int):
    # Creating two 100x100 matrices using NumPy arrays
    A_np = np.random.rand(n, n)
    B_np = np.random.rand(n, n)
    
    # Matrix multiplication using NumPy
    start_time = time.time()
    _ = np.dot(A_np, B_np)
    return time.time() - start_time


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import sys

    # hack to ensure we are executing in the same
    import os
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)
    # print("pwd={}".format(os.getcwd()))

    N = range(10, 200, 10)
    python_times = []
    numpy_times = []
    for n in N:
        sys.stdout.write("%d " % n)
        sys.stdout.flush()
        python_time = mult_nxn(n)
        numpy_time = numpy_nxn(n)
        python_times.append(python_time)
        numpy_times.append(numpy_time)

    plt.scatter(N, python_times, color="blue")
    plt.scatter(N, numpy_times, color="red")

    plt.title("Execution times")
    plt.xlabel("N")
    plt.ylabel("seconds")
    plt.show()

    N2 = range(10, 1400, 50)
    numpy_times = []
    for n in N2:
        numpy_time = numpy_nxn(n)
        numpy_times.append(numpy_time)

    plt.scatter(N2, numpy_times, color="red")
    plt.scatter(N, python_times, color="blue")

    plt.ylim(0, 0.035)
    plt.title("Execution times")
    plt.xlabel("N")
    plt.ylabel("seconds")
    plt.show()

  
