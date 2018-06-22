import bpy
from helper import *
from math import pi
from dash import Dash

class Path(object):
    def __init__(self, start, end):
        angles = orientationOfVector(start, end)
        magnitude = (end - start).magnitude
        normal = (end - start)/magnitude

        middle = start + 0.5*(end - start)

        reminder = magnitude/2
        n = 0
        
        self._dashes = []

        while reminder >= 0.3:
            dash = Dash(middle+(0.15+n)*normal, 0.1, 0.05, angles[0] - pi/2, angles[1])
            self._dashes.append(dash)
            dash = Dash(middle-(0.15+n)*normal, 0.1, 0.05, angles[0] - pi/2, angles[1])
            self._dashes.append(dash)
            reminder -= 0.3
            n += 0.3


    def delete(self):
        for dash in self._dashes:
            dash.delete()
