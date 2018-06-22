from monkey import Monkey
from grid import Grid
from kicker import Kicker
from world import World
from mathutils import Vector
from config import Config
import bpy

def first():
	monkeyData = (Vector((0,0,0)), Vector((1,1,0)), Vector((0,0,0)))
	gridData = 9
	modeData = False	
	kickersData = []
	kickersData.append((Vector((4,4,0)), Vector((-2,2,0))))
	kickersData.append((Vector((2,6,0)), Vector((3,0,0))))
	kickersData.append((Vector((8,6,0)), Vector((-1,-1,0))))
	kickersData.append((Vector((3,1,0)), Vector((-2,2,0))))
	kickersData.append((Vector((1,3,0)), Vector((0,1,0))))
	kickersData.append((Vector((1,3,0)), Vector((0,1,0))))
	kickersData.append((Vector((1,7,0)), Vector((1,0,0))))
	kickersData.append((Vector((7,7,0)), Vector((0,-1,0))))
	config = Config(gridData, kickersData, monkeyData, modeData)
	world = World(config)

def custom():
	monkeyData = (Vector((1,1,0)), Vector((0,0,0)), Vector((0,0,0)))
	gridData = 9
	modeData = True
	kickersData = []
	kickersData.append((Vector((1,1,0)), Vector((3,0,0))))
	kickersData.append((Vector((4,1,0)), Vector((2,2,0))))
	config = Config(gridData, kickersData, monkeyData, modeData)
	world = World(config)
