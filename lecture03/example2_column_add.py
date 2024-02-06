import pandas as pd
import numpy as np
from numpy import random
import time


def python_add_c(c:int, n:int):
    arr = [random.rand() for _ in range(n)]
    new_arr = [0] * n
    start_time = time.time()
    for i in range(len(arr)):
        new_arr[i] = arr[i] + c
    end_time = time.time()

    return end_time - start_time


def numpy_add_c(c: int, n: int):
    A = np.array([random.rand() for _ in range(n)])
    start_time = time.time()
    A = A + c
    end_time = time.time()
    return end_time - start_time


def column_add_c(c: int, n: int) -> float:

    x = np.arange(n)  # Generate index values for x
    y = np.random.rand(n)  # Generates n random numbers between 0 and 1
    df = pd.DataFrame({'y': y}, index=x)

    start_time = time.time()
    df["newy"] = df["y"] + c
    end_time = time.time()

    return end_time - start_time

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import sys

    # hack to ensure we are executing in the same
    import os
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)
    # print("pwd={}".format(os.getcwd()))

    N = range(1000, 10000, 100)
    numpy_times = []
    python_times = []
    column_times = []
    for n in N:
        sys.stdout.write("..")
        sys.stdout.flush()
        python_times.append(python_add_c(5, n))
        numpy_times.append(numpy_add_c(5, n))
        column_times.append(column_add_c(5, n))

    # open the results from C.
    # c_n, c_times = read_c_lang_results("example_1_array_c_output.csv")

    plt.scatter(N, python_times, color="blue")
    plt.scatter(N, numpy_times, color="red")
    plt.scatter(N, column_times, color="black")

    plt.title("Execution times")
    plt.xlabel("N")
    plt.ylabel("seconds")
    plt.show()

    N2 = range(1000, 100000, 1000)
    numpy_times = []
    column_times = []
    for n in N2:
        sys.stdout.write(".")
        sys.stdout.flush()
        numpy_times.append(numpy_add_c(5, n))
        column_times.append(column_add_c(5, n))

    # c_n, c_times = read_c_lang_results(
    #    "example_1_array_c_big_output.csv")
    plt.scatter(N, python_times, color="blue")
    plt.scatter(N2, numpy_times, color="red")
    plt.scatter(N2, column_times, color="black")

    plt.title("Execution times")
    plt.xlabel("N")
    plt.ylabel("seconds")
    plt.show()
