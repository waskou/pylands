import bpy
import math
from helper import *

class Arrow(object):
    def __init__(self, start, end, r1, r2):
        angles = orientationOfVector(start, end)

        bpy.ops.mesh.primitive_cone_add(
            radius1 = r1, 
            depth = (end - start).magnitude,
            location = start + 0.5*(end - start)
        ) 

        bpy.context.object.rotation_euler[1] = angles[0]
        bpy.context.object.rotation_euler[2] = angles[1]

        self._body = bpy.context.object
            
        bpy.ops.mesh.primitive_cone_add(
            radius1 = r2, 
            depth = 0.2*(end-start).magnitude,
            location = start + 0.9*(end - start)   
        )
        
        bpy.context.object.rotation_euler[1] = angles[0] 
        bpy.context.object.rotation_euler[2] = angles[1]

        self._head = bpy.context.object

    def delete(self):
        self._head.select = True
        bpy.ops.object.delete()

        self._body.select = True
        bpy.ops.object.delete()
