class Config(object):
    def __init__(self, gridData, kickersData, monkeyData, modeData):
        self._gridData = gridData
        self._monkeyData = monkeyData
        self._kickersData = kickersData
        self._modeData = modeData

    @property
    def kickersData(self):
        return self._kickersData
    @property
    def monkeyData(self):
        return self._monkeyData
    @property
    def gridData(self):
        return self._gridData
    @property
    def modeData(self):
        return self._modeData
