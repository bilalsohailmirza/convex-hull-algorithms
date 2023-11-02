import random
from matplotlib import pyplot as plt


def initPoints(n):
    Points = []
    for i in range(0, n):  # Plots points on table
        Points.append(
            (random.randint(1, 100), random.randint(1, 100))
        )  # Change bounds to increase or decrease
    return Points


def isPoint(point, *args):
    for arg in args:
        if point[0] == arg[0] and point[1] == arg[1]:
            return True
    return False


def areaTriangle(A, B, C):
    partial_A: int = A[0] * (B[1] - C[1])
    partial_B: int = B[0] * (C[1] - A[1])
    partial_C: int = C[0] * (A[1] - B[1])
    area: float = (partial_A + partial_B + partial_C) / 2.0
    area = abs(area)
    return area


def areaQuadrilateral(A, B, C, D):
    total_area: int = A[0] * B[1] + B[0] * C[1] + C[0] * D[1] + D[0] * A[1]
    extra_area: int = B[0] * A[1] + C[0] * B[1] + D[0] * C[1] + A[0] * D[1]
    area: float = (total_area - extra_area) / 2.0
    return abs(area)


def PointElimination(Points, N):
    x_sortedPoints = sorted(Points, key=lambda x: x[0])
    y_sortedPoints = sorted(Points, key=lambda x: x[1])

    left_most = x_sortedPoints[0]
    right_most = x_sortedPoints[-1]
    lowest = y_sortedPoints[0]
    highest = y_sortedPoints[-1]
    plt.plot([left_most[0], lowest[0]], [left_most[1], lowest[1]])
    plt.plot([left_most[0], highest[0]], [left_most[1], highest[1]])
    plt.plot([right_most[0], lowest[0]], [right_most[1], lowest[1]])
    plt.plot([right_most[0], highest[0]], [right_most[1], highest[1]])

    outside_points = []
    for i in range(0, len(Points)):
        point = Points[i]
        if not isPoint(point, left_most, right_most, lowest, highest):
            sum_of_triangles = 0
            sum_of_triangles += areaTriangle(highest, point, right_most)
            sum_of_triangles += areaTriangle(right_most, point, lowest)
            sum_of_triangles += areaTriangle(lowest, point, left_most)
            sum_of_triangles += areaTriangle(left_most, point, highest)
            quadrilateral = areaQuadrilateral(highest, right_most, lowest, left_most)
            if sum_of_triangles != quadrilateral:
                outside_points.append(point)

    outside_points.append(highest)
    outside_points.append(lowest)
    outside_points.append(right_most)
    outside_points.append(left_most)

    x_sortedPoints = sorted(outside_points, key=lambda x: x[0])
    y_sortedPoints = sorted(outside_points, key=lambda x: x[1])
    inside_points = []

    top_right = highest
    for point in reversed(y_sortedPoints):
        if point[0] > highest[0] and point[1] > right_most[1]:
            top_right = point
            break
    top_left = highest
    for point in reversed(y_sortedPoints):
        if point[0] < highest[0] and point[1] > left_most[1]:
            top_left = point
            break
    bottom_right = lowest
    for point in y_sortedPoints:
        if point[0] > lowest[0] and point[1] < right_most[1]:
            bottom_right = point
            break
    bottom_left = lowest
    for point in y_sortedPoints:
        if point[0] < lowest[0] and point[1] < left_most[1]:
            bottom_left = point
            break

    if not isPoint(top_right, highest, right_most):
        plt.plot([top_right[0], highest[0]], [top_right[1], highest[1]])
        plt.plot([top_right[0], right_most[0]], [top_right[1], right_most[1]])
    if not isPoint(top_left, highest, left_most):
        plt.plot([top_left[0], highest[0]], [top_left[1], highest[1]])
        plt.plot([top_left[0], left_most[0]], [top_left[1], left_most[1]])
    if not isPoint(bottom_right, lowest, right_most):
        plt.plot([bottom_right[0], lowest[0]], [bottom_right[1], lowest[1]])
        plt.plot([bottom_right[0], right_most[0]], [bottom_right[1], right_most[1]])
    if not isPoint(bottom_left, lowest, left_most):
        plt.plot([bottom_left[0], lowest[0]], [bottom_left[1], lowest[1]])
        plt.plot([bottom_left[0], left_most[0]], [bottom_left[1], left_most[1]])

    if not isPoint(top_right, highest, right_most):
        for point in outside_points:
            sum_of_triangles = 0
            sum_of_triangles += areaTriangle(top_right, point, right_most)
            sum_of_triangles += areaTriangle(right_most, point, highest)
            sum_of_triangles += areaTriangle(highest, point, top_right)
            outer_triangle = areaTriangle(highest, top_right, right_most)
            if sum_of_triangles == outer_triangle:
                inside_points.append(point)

    if not isPoint(bottom_right, lowest, right_most):
        for point in outside_points:
            sum_of_triangles = 0
            sum_of_triangles += areaTriangle(bottom_right, point, lowest)
            sum_of_triangles += areaTriangle(lowest, point, right_most)
            sum_of_triangles += areaTriangle(right_most, point, bottom_right)
            outer_triangle = areaTriangle(right_most, bottom_right, lowest)
            if sum_of_triangles == outer_triangle:
                inside_points.append(point)

    if not isPoint(bottom_left, lowest, left_most):
        for point in outside_points:
            sum_of_triangles = 0
            sum_of_triangles += areaTriangle(bottom_left, point, lowest)
            sum_of_triangles += areaTriangle(lowest, point, left_most)
            sum_of_triangles += areaTriangle(left_most, point, bottom_left)
            outer_triangle = areaTriangle(left_most, bottom_left, lowest)
            if sum_of_triangles == outer_triangle:
                inside_points.append(point)

    if not isPoint(top_left, highest, left_most):
        for point in outside_points:
            sum_of_triangles = 0
            sum_of_triangles += areaTriangle(top_left, point, left_most)
            sum_of_triangles += areaTriangle(left_most, point, highest)
            sum_of_triangles += areaTriangle(highest, point, top_left)
            outer_triangle = areaTriangle(highest, top_left, left_most)
            if sum_of_triangles == outer_triangle:
                inside_points.append(point)

    outside_points = list(set(outside_points).difference(set(inside_points)))

    for point in outside_points:
        plt.plot(point[0], point[1], ".r")


def main():
    # try:
    #     N = int(sys.argv[1])
    # except:
    #     N = int(input("Introduce N: "))
    N = 1000
    Points = initPoints(N)

    PointElimination(Points, N)
    plt.show()


if __name__ == "__main__":
    main()
