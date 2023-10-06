import random
import time

def convex_hull(points):
    def quick_hull(points):
        if len(points) <= 3:
            return points

        min_x = min(points, key=lambda p: p[0])
        max_x = max(points, key=lambda p: p[0])

        left_points = [point for point in points if (point[0] - min_x[0]) * (max_x[1] - min_x[1]) - (max_x[0] - min_x[0]) * (point[1] - min_x[1]) > 0]
        right_points = [point for point in points if (point[0] - min_x[0]) * (max_x[1] - min_x[1]) - (max_x[0] - min_x[0]) * (point[1] - min_x[1]) < 0]

        left_hull = quick_hull(left_points)
        right_hull = quick_hull(right_points)

        return left_hull + right_hull

    if len(points) < 3:
        return points

    points.sort() 
    return quick_hull(points)

num_points = 5
points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_points)]

start_time = time.time()
convex_hull(points)
end_time = time.time()

execution_time_us = (end_time - start_time) * 1e6 
print(f"점의 개수: {num_points}")
print(f"Convex Hull 계산 시간: {execution_time_us:.2f} 마이크로초")
