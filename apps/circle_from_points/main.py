from apps.circle_from_points.input import parse_points
from geom2d import make_circle_from_points

if __name__ == "__main__":
    (a,b,c) = parse_points()
    circle = make_circle_from_points(a, b, c)
    print(circle)