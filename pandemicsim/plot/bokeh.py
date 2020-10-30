from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
import time
from pandemicsim.plot.base import BasePlotter


class BokehPlotter(BasePlotter):
    def __init__(self, *args):
        super().__init__(*args)
        positions = self.space.get_positions()
        self.map = ColumnDataSource(data=dict(x=positions[:, 0], y=positions[:, 1]))
        self.fig = figure(x_axis_label="X", y_axis_label="Y")
        self.graph = self.fig.circle(source=self.map, color='blue')

    def plot(self):
        positions = self.space.get_positions()
        # self.map.data = dict(x=positions[:, 0], y=positions[:, 1])
        self.graph.data_source.stream(dict(x=positions[:, 0], y=positions[:, 1]))
        time.sleep(0.05)
