import time
import math

def run_code(n):
    sum_result = 0
    j = 5
    while j < n/2:
        k = 5
        while k < n:
            k = k * math.sqrt(2)
        j = math.sqrt(3) * j
    return sum_result

# Define a range of input sizes (e.g., powers of 2)
input_sizes = [2**i for i in range(1, 21)]

# Measure execution time for each input size
for n in input_sizes:
    start_time = time.time()
    result = run_code(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Input size n = {n}: Execution time = {execution_time:.6f} seconds")

# You can now analyze the results to estimate the time complexity