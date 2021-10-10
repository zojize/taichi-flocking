# TODO
import taichi as ti


@ti.data_oriented
class Rect:
    def __init__(self, x, y, w, h) -> None:
        self._x = x
        self._y = y
        self._w = w
        self._h = h


class QuadTree:
    def __init__(self) -> None:
        pass
