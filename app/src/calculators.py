
class CalculatorBase():
    def __init__(self, data, frame_tube, door_tube, frame_gap=10, fill_gap=5):
        self._data = data
        self._width = int(data['width'])
        self._height = int(data['height'])
        self._cliarance = int(data['cliarance'])
        self._bridge = int(data['bridge_height'])
        self._frame_tube = frame_tube  # (y, x)
        self._door_tube = door_tube  # (y, x)
        self._frame_gap = frame_gap
        self._fill_gap = fill_gap

        self._door_width = 0
        self._door_height = 0
        self._door_fill_width = 0
        self._door_fill_height = 0
        self._bridge_fill_width = 0
        self._bridge_fill_height = 0

    def run(self):
        self._calculate_sizes()
        self._save_to_data()

    def _save_to_data(self):
        self._data['cliarance'] = str(self._cliarance)
        self._data['door_width'] = str(self._door_width)
        self._data['door_height'] = str(self._door_height)
        self._data['door_fill_width'] = str(self._door_fill_width)
        self._data['door_fill_height'] = str(self._door_fill_height)
        self._data['bridge_fill_width'] = str(self._bridge_fill_width)
        self._data['bridge_fill_height'] = str(self._bridge_fill_height)

    def _calculate_sizes(self):
        self._calc_cliarance()
        self._calc_door_width()
        self._calc_door_height()
        self._calc_door_fill_width()
        self._calc_door_fill_height()
        self._calc_bridge_fill_width()
        self._calc_bridge_fill_height()

    def _calc_cliarance(self):
        pass

    def _calc_door_width(self):
        self._door_width = self._width - self._frame_tube[1] * 2 - self._frame_gap * 2

    def _calc_door_height(self):
        self._door_height = self._height - self._cliarance - self._door_tube[1] - self._frame_gap

    def _calc_door_fill_width(self):
        self._door_fill_width = self._door_width - self._door_tube[1] * 2 - self._fill_gap

    def _calc_door_fill_height(self):
        self._door_fill_height = self._door_height - self._door_tube[1] * 2 - self._fill_gap

    def _calc_bridge_fill_width(self):
        pass

    def _calc_bridge_fill_height(self):
        pass


class CalculatorBridgeY(CalculatorBase):
    def __init__(self, data, frame_tube, door_tube, frame_gap=10, fill_gap=5):
        super().__init__(data, frame_tube, door_tube, frame_gap, fill_gap)


class CalculatorBridgeN(CalculatorBase):
    def __init__(self, data, frame_tube, door_tube, frame_gap=10, fill_gap=5):
        super().__init__(data, frame_tube, door_tube, frame_gap, fill_gap)

    def _calc_door_height(self):
        self._door_height = self._height - self._cliarance


class CalculatorBridgeYS(CalculatorBase):
    def __init__(self, data, frame_tube, door_tube, frame_gap=10, fill_gap=5):
        super().__init__(data, frame_tube, door_tube, frame_gap, fill_gap)

    def _calc_cliarance(self):
        self._cliarance = self._frame_tube[1] + self._frame_gap

    def _calc_door_height(self):
        self._door_height = self._height - self._door_tube[1] * 2 - self._frame_gap * 2


class CalculatorBridgeT(CalculatorBase):
    def __init__(self, data, frame_tube, door_tube, frame_gap=10, fill_gap=5):
        super().__init__(data, frame_tube, door_tube, frame_gap, fill_gap)

    def _calc_door_height(self):
        self._door_height = self._height - self._cliarance - self._bridge - self._frame_gap

    def _calc_bridge_fill_width(self):
        self._bridge_fill_width = self._width - self._frame_tube[1] * 2 - self._fill_gap

    def _calc_bridge_fill_height(self):
        self._bridge_fill_height = self._bridge - self._frame_tube[1] * 2 - self._fill_gap