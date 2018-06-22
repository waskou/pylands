import bpy
from plate import Plate
from path import Path
from mathutils import Matrix
import math
from mathutils import Vector
        
class Monkey(object):
    def __init__(self, pos, vel, acc):
        self._pos = pos
        self._vel = vel
        self._acc = acc
        bpy.ops.mesh.primitive_monkey_add(location = pos)
        bpy.context.object.scale *= 0.2
        self._monkey = bpy.context.object
        self._platesTrail = []
        self._pathsTrail = []
        initPlate = Plate(0.2, self._pos)
        self._platesTrail.append(initPlate)
        
    @property
    def monkey(self):
        return self._monkey
    @property
    def pos(self):
        return self._pos    
    @property
    def vel(self):
        return self._vel    
    @property
    def acc(self):
        return self._acc
    @pos.setter
    def pos(self, value):
        self._pos = value        
    @vel.setter
    def vel(self, value):
        self._vel = value        
    @acc.setter
    def acc(self, value):
        self._acc = value
                
    def move(self, imposed_vel):
        self._vel = imposed_vel
        self._pos += self._vel
        self._monkey.location = self._pos
        plate = Plate(0.2, self._pos)
        self._platesTrail.append(plate)
        path = Path(self._pos - self._vel, self._pos)
        self._pathsTrail.append(path)

    def evolve(self):
        self.move(self._vel)

    def evolveCustom(self):
        mat = Matrix.Rotation(math.pi / 2, 4, "Z")
        self._vel.rotate(mat)
        self.move(self._vel)

    def delete(self, pos, vel, acc):
        for plate in self._platesTrail:
            plate.delete()
        for path in self._pathsTrail:
            path.delete()
        self._monkey.select = True
        bpy.ops.object.delete()
        self._pos = pos
        self._vel = vel
        self._acc = acc
        
