import time
import math

def run_option5(n):
    j = 5
    while j < n/2:
        k = 5
        while k < n:
         #  sum += a[j] * b[k]
            k = k * math.sqrt(2)
        j = math.sqrt(3) * j

input = [10**i for i in [1, 3, 6, 9, 12]]

for n in input:
    start_time = time.perf_counter()
    run_option5(n)
    end_time = time.perf_counter()
    time_s = end_time - start_time
    time_ns = time_s * 1e9
    print(f"n = {n}: time = {time_ns:.2f} ns")
