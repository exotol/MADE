from math import atan2

EPS = 1e-5


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, a, b):
        if isinstance(a, Point) and isinstance(b, Point):
            self.x = b.x - a.x
            self.y = b.y - a.y
        else:
            self.x = a
            self.y = b
        self.angle = self._angle()
        self.r = self._r()

    def __add__(self, other):
        """+ is sum of vectors"""
        return Vector(self.x + other.x, self.y + other.y)

    def __neg__(self):
        """- is a unary minus for vectors"""
        return Vector(-self.x, -self.y)

    def __mul__(self, other):
        """* is a dot product of vectors"""
        return self.x * other.x + self.y * other.y

    def __matmul__(self, other):
        """@ is a cross product of vectors"""
        return self.x * other.y - self.y * other.x

    def __xor__(self, other):
        """^ is the angle between vectors"""
        return atan2(self @ other, self * other)

    def _angle(self):
        """polar angle of vector"""
        return atan2(self.y, self.x)

    def _r(self):
        """length of vector"""
        return (self * self) ** 0.5


def point_on_segment(p, a, b):
    pa = Vector(p, a)
    pb = Vector(p, b)
    return pa * pb < EPS and abs(pa @ pb) < EPS


def main():
    p_x, p_y, a_x, a_y, b_x, b_y = map(int, input().split())
    p = Point(p_x, p_y)
    a = Point(a_x, a_y)
    b = Point(b_x, b_y)
    print("YES" if point_on_segment(p, a, b) else "NO")


if __name__ == "__main__":
    main()
