import bpy

class Grid(object): 

    def __init__(self, size):
        self._size = size
        self._points = []
        for x in range(0, self._size):
            for y in range(0, self._size):
                point = addPointAt(x, y, 0)
                self._points.append(point)

    @property
    def size(self):
        return self._size

    def delete(self):
        for point in self._points:
            point.select = True
            bpy.ops.object.delete()

def addPointAt(x, y, z):
    bpy.ops.mesh.primitive_plane_add(location=(x,y,z))
    obj = bpy.context.object
    obj.scale *= 0.05
    return obj


