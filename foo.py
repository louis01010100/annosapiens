#!/usr/bin/env python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({} {})".format(self.x, self.y)


point = Point(10, 10)

print(point)