import random   # to generate points radomly
import timeit   # to calculate the time complexity

def divide_conquer(points):
    def convex_hull(points):
        if len(points) <= 3:    # Convex polygons created by up to 3 points return the value as it is because there are no additional points inside
            return points

        min_x = min(points, key=lambda p: p[0])     
        max_x = max(points, key=lambda p: p[0])

        left_points = [point for point in points if (point[0] - min_x[0]) * (max_x[1] - min_x[1]) - (max_x[0] - min_x[0]) * (point[1] - min_x[1]) < 0]
        right_points = [point for point in points if (point[0] - min_x[0]) * (max_x[1] - min_x[1]) - (max_x[0] - min_x[0]) * (point[1] - min_x[1]) > 0]

        P1 = convex_hull(left_points)
        P2 = convex_hull(right_points)

        return P1 + P2

    if len(points) < 3:
        return points

    points.sort()  # x 좌표순으로 정렬
    return convex_hull(points)

# 점의 개수를 원하는 대로 변경
num_points = 2
points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_points)]

# Convex Hull 계산 시간 측정 (밀리초 단위)
execution_time = timeit.timeit(lambda: divide_conquer(points), number=1)
execution_time_ms = execution_time * 1e6  # 초를 밀리초로 변환

# 시간 복잡도 출력
print(f"점의 개수: {num_points}")
print(f"Convex Hull 계산 시간: {execution_time_ms:.2f} 밀리초")