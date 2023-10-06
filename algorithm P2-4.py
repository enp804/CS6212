import random   # to generate points radomly
import timeit   # to calculate the time complexity

def divide_conquer(points):
    def convex_hull(points):
        # recusion
        if len(points) <= 3:    # Convex polygons created by up to 3 points return the value as it is because there are no additional points inside
            return points

        min_x = min(points, key=lambda p: p[0])     
        max_x = max(points, key=lambda p: p[0])
        min_y = min(points, key=lambda p: p[1])
        max_y = max(points, key=lambda p: p[1])

        # Distinguish where a particular point belongs
        left_points = [point for point in points if (point[0] - min_x[0]) * (max_y[1] - min_y[1]) - (max_x[0] - min_x[0]) * (point[1] - min_y[1]) < 0]
        right_points = [point for point in points if (point[0] - min_x[0]) * (max_y[1] - min_y[1]) - (max_x[0] - min_x[0]) * (point[1] - min_y[1]) > 0]

        # subsets P1, P2
        P1 = convex_hull(left_points)
        P2 = convex_hull(right_points)

        # merge subsets
        return P1 + P2

    if len(points) < 3:
        return points

    # Sort by x-coordinate
    points.sort()
    return convex_hull(points)

# Specify the number of points
point_num = 5
points = [(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(point_num)]

# Calculate time complexity
exec_time = timeit.timeit(lambda: divide_conquer(points), number=1) * 1e6

# display
print(f"Number of points: {point_num}, Time complexity: {exec_time:.2f} microsec")