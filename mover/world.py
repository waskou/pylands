import bpy
import kicker
import monkey
from monkey import Monkey
from config import Config
from grid import Grid
from kicker import Kicker
from mathutils import Vector

class World(object):
    def __init__(self, config):
        self._config = config
        self.initialize(self._config)
        self.evolve(self._config.modeData)  

    @property
    def kickers(self):
        return self._kickers
    @property
    def monkey(self):
        return self._monkey
    @property
    def grid(self):
        return self._grid

    def initialize(self, config):
        self._monkey = Monkey(config.monkeyData[0], config.monkeyData[1], config.monkeyData[2])
        self._grid = Grid(config.gridData)
        self._kickers = []
        print(self._config.kickersData)
        for kickerData in self._config.kickersData:
            kicker = Kicker(kickerData[0], kickerData[1])
            self._kickers.append(kicker)
        self.createKickers()

    def createKickers(self):
        for kicker in self._kickers:
            kicker.create()

    def evolve(self, isCustom):
        def handler(scene):
            frame = scene.frame_current
            if frame in range(0, 250, 10):
                metKicker = 0          
                for kicker in self._kickers:
                    if kicker.pos == self._monkey.pos:
                        self._monkey.move(kicker.strenght)
                        metKicker = 1
                        break
                if metKicker == 0:
                    if isCustom:
                        self._monkey.evolveCustom()
                    else:
                        self._monkey.evolve()
            elif frame == 250:
                self.delete()
                bpy.app.handlers.frame_change_pre.clear()

        bpy.app.handlers.frame_change_pre.clear()
        bpy.app.handlers.frame_change_pre.append(handler)

    def delete(self):
        self._monkey.delete(self._config.monkeyData[0], self._config.monkeyData[1], self._config.monkeyData[2])
        self._monkey = None
        for kicker in self._kickers:
            kicker.delete()
        self._kickers = None
        self._grid.delete()
        self._grid = None