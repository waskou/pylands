import bpy
import math

def orientationOfVector(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    dz = end[2] - start[2]   
    dist = math.sqrt(dx**2 + dy**2 + dz**2)

    theta = math.acos(dz/dist)            
    phi = math.atan2(dy, dx)

    result = []
    result.append(theta)
    result.append(phi)
    
    return result

def makeRedTransparent(obj):
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.mode_set(mode = 'OBJECT')

    mat = bpy.data.materials.new(name="TRANSPARENT_RED")
    mat.use_transparency = True
    mat.transparency_method = 'Z_TRANSPARENCY'
    mat.alpha = 0.5

    obj.data.materials.append(mat) 
    obj.active_material.diffuse_color = (1, 0, 0)
    obj.show_transparent = True