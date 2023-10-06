import time
import math

def run_option5(n):
    j = 5
    while j < n/2:
        k = 5
        while k < n:
            k = k * math.sqrt(2)
        j = math.sqrt(3) * j

input = [10**i for i in range(1, 6)]

for n in input:
    start_time = time.perf_counter()
    run_option5(n)
    end_time = time.perf_counter()
    execution_time_seconds = end_time - start_time
    execution_time_nanoseconds = execution_time_seconds * 1e9
    print(f"Input size n = {n}: Execution time = {execution_time_nanoseconds:.2f} ns")

