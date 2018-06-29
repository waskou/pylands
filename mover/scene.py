import bpy
from config import Config
from grid import Grid
from monkey import Monkey


class Scene(object):
	def __init__(self, config, trajectory):
		self.animate(config, trajectory)
		self._monkey = None

	def animate(self, config, trajectory):

		def handler(scene):
			frame = scene.frame_current
			if frame ==  10:
				self._grid = Grid(config.gridData)
				
			elif frame == 20:
				self._monkey = Monkey(config.monkeyData[0], config.monkeyData[1], config.monkeyData[2])

			n = 0

			for frame in range(40,80,10):
				moveVel = trajectory[n] - self._monkey.pos
				self._monkey.move(moveVel)
				n += 1
				print(n)
				break

			if frame == 250:
				self._monkey.delete(config.monkeyData[0], config.monkeyData[1], config.monkeyData[2])

		bpy.app.handlers.frame_change_pre.clear()
		bpy.app.handlers.frame_change_pre.append(handler)

