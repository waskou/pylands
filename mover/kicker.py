import bpy
from arrow import Arrow

class Kicker(object):
    def __init__(self, pos, strenght):
        self._pos = pos
        self._strenght = strenght
        self._arrow = None

    @property
    def pos(self):
        return self._pos
    @property
    def strenght(self):
        return self._strenght
    @pos.setter
    def pos(self, value):
        self._pos = value
    @strenght.setter
    def strenght(self, value):
        self._strenght = value

    def create(self):
        self._arrow = Arrow(self._pos, self._pos + self._strenght, 0.04, 0.06)

    def delete(self):
        self._arrow.delete()
        self._arrow = None

