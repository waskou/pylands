import bpy
from helper import *

class Plate(object):
    def __init__(self, r, loc):
        bpy.ops.mesh.primitive_circle_add(location = loc)
        obj = bpy.context.object
        obj.scale *= r
        makeRedTransparent(obj)
        self._obj = obj
    
    def delete(self):
        self._obj.select = True
        bpy.ops.object.delete()
        

