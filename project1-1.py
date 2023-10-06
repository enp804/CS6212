import timeit
import math

def run_code(n, a, b):
    sum_result = 0
    j = 5
    while j < n/2:
        k = 5
        while k < n:
            sum_result += a[j] * b[k]
            k = k * math.sqrt(2)
        j = math.sqrt(3) * j
    return sum_result

# Replace this with your own data or generate sample data
a = [0] * 10000
b = [0] * 10000

# Define a range of input sizes (e.g., powers of 2)
input_sizes = [2**i for i in range(10, 21)]

# Measure execution time for each input size using timeit
for n in input_sizes:
    setup_code = f"from __main__ import run_code, a, b, math; n = {n}"
    execution_time = timeit.timeit("run_code(n, a, b)", setup=setup_code, number=10)
    print(f"Input size n = {n}: Average execution time = {execution_time/10:.6f} seconds")

# You can now analyze the results to estimate the time complexity