import random   # to generate points radomly
import timeit   # to calculate the time complexity

def divide_conquer(n):
    def convex_hull(n):
        # recusion
        if len(n) <= 3:    # Convex polygons created by up to 3 points return the value as it is because there are no additional points inside
            return n

        min_x = min(n, key=lambda p: p[0])     
        max_x = max(n, key=lambda p: p[0])
        min_y = min(n, key=lambda p: p[1])
        max_y = max(n, key=lambda p: p[1])

        # Distinguish where a particular point belongs
        left_n = [x for x in n if (x[0] - min_x[0]) * (max_y[1] - min_y[1]) - (max_x[0] - min_x[0]) * (x[1] - min_y[1]) < 0]
        right_n = [x for x in n if (x[0] - min_x[0]) * (max_y[1] - min_y[1]) - (max_x[0] - min_x[0]) * (x[1] - min_y[1]) > 0]

        # subsets P1, P2
        P1 = convex_hull(left_n)
        P2 = convex_hull(right_n)

        # merge subsets
        return P1 + P2

    if len(n) < 3:
        return n

    # Sort by x-coordinate
    n.sort()
    return convex_hull(n)

# Specify the number of points
point_num = 5
n = [(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(point_num)]

# Calculate time complexity
exec_time = timeit.timeit(lambda: divide_conquer(n), number=1) * 1e6

# display
print(f"Number of points: {point_num}, Time complexity: {exec_time:.2f} microsec")