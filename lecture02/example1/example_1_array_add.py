import numpy as np
import time
from numpy import random
import csv


def python_add_constant():
    array = [1, 2, 3, 4, 5]
    new_array = [0] * len(array)
    for i in range(len(array)):
        new_array[i] = array[i] + 5

    print("Original array:", array)
    print("New array:", new_array)


def numpy_add_constant():
    # Create a one-dimensional NumPy array
    array = np.array([1, 2, 3, 4, 5])

    # Add constant to all elements of the array
    new_array = array + 5

    # Display the original and the new array
    print("Original array:", array)
    print("New array:", new_array)


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


def read_c_lang_results(csv_file):
    n_values = []
    t_values = []

    # Open the CSV file and read the data
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
    
        # Skip the header row
        next(csvreader)
    
        # Read each row and append the values to the lists
        for row in csvreader:
            n_values.append(int(row[0]))  # Convert n to integer
            t_values.append(float(row[1]))  # Convert function result to float

    return n_values, t_values


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import sys

    # hack to ensure we are executing in the same
    import os
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)
    # print("pwd={}".format(os.getcwd()))

    # python_add_constant()
    # numpy_add_constant()

    N = range(1000, 10000, 100)
    numpy_times = []
    python_times = []
    for n in N:
        sys.stdout.write("..")
        sys.stdout.flush()
        python_times.append(python_add_c(5, n))
        numpy_times.append(numpy_add_c(5, n))

    # open the results from C.
    c_n, c_times = read_c_lang_results("example_1_array_c_output.csv")

    plt.scatter(N, python_times, color="blue")
    plt.scatter(N, numpy_times, color="red")
    plt.scatter(c_n, c_times, color="green")

    plt.title("Execution times")
    plt.xlabel("N")
    plt.ylabel("seconds")
    plt.show()

    N2 = range(1000, 100000, 1000)
    numpy_times = []
    for n in N2:
        sys.stdout.write(".")
        sys.stdout.flush()
        numpy_times.append(numpy_add_c(5, n))

    c_n, c_times = read_c_lang_results(
        "example_1_array_c_big_output.csv")
    plt.scatter(N, python_times, color="blue")
    plt.scatter(N2, numpy_times, color="red")
    plt.scatter(c_n, c_times, color="green")

    plt.title("Execution times")
    plt.xlabel("N")
    plt.ylabel("seconds")
    plt.show()

