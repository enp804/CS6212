import random
import timeit

# D&C 알고리즘을 사용한 Convex Hull 계산 코드
def convex_hull(points):
    def quick_hull(points):
        if len(points) <= 3:
            return points

        min_x = min(points, key=lambda p: p[0])
        max_x = max(points, key=lambda p: p[0])

        left_points = [point for point in points if (point[0] - min_x[0]) * (max_x[1] - min_x[1]) - (max_x[0] - min_x[0]) * (point[1] - min_x[1]) > 0]
        right_points = [point for point in points if (point[0] - min_x[0]) * (max_x[1] - min_x[1]) - (max_x[0] - min_x[0]) * (point[1] - min_x[1]) < 0]

        upper_hull = quick_hull(left_points)
        lower_hull = quick_hull(right_points)

        return upper_hull + lower_hull

    if len(points) < 3:
        return points

    points.sort()  # x 좌표순으로 정렬
    return quick_hull(points)

# 점의 개수를 원하는 대로 변경
num_points = 5
points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_points)]

# Convex Hull 계산 시간 측정 (밀리초 단위)
execution_time = timeit.timeit(lambda: convex_hull(points), number=1)
execution_time_ms = execution_time * 1e6  # 초를 밀리초로 변환

# 시간 복잡도 출력
print(f"점의 개수: {num_points}")
print(f"Convex Hull 계산 시간: {execution_time_ms:.2f} 밀리초")