import bpy
from helper import *

class Dash(object):
    def __init__(self, loc, xScale, yScale, theta, phi):
        bpy.ops.mesh.primitive_plane_add(location = loc)
        obj = bpy.context.object
        obj.scale.x = xScale
        obj.scale.y = yScale
        obj.rotation_euler[1] = theta
        obj.rotation_euler[2] = phi
        makeRedTransparent(obj)

        self._dash = obj

    def delete(self):
        self._dash.select = True
        bpy.ops.object.delete()

