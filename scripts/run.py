import argparse
import time
from bokeh.io import curdoc
from bokeh.client import push_session, show_session
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from pandemicsim.models import Pandemic


def parse_args():
    parser = argparse.ArgumentParser(
        description="Get parameters for the ABM Simulation"
    )

    # Name and seed
    parser.add_argument("--name", help="experiment name")
    parser.add_argument("--seed", help="seed for reproducibility", type=int, default=42)
    parser.add_argument("--width", help="width", type=float, default=150)
    parser.add_argument("--height", help="height", type=float, default=100)

    return parser.parse_args()


if __name__ == "__main__":
    config = parse_args()

    session = push_session(curdoc())
    model = Pandemic()

    positions = model.space.get_positions()
    pos_map = ColumnDataSource(data=dict(x=positions[:, 0], y=positions[:, 1]))
    fig = figure(x_axis_label="X", y_axis_label="Y")
    graph = fig.circle(source=pos_map, color='blue')
    session.show(fig)
    session.loop_until_closed()

    for _ in range(5):
        model.step()
        positions = model.space.get_positions()
        graph.data_source.stream(dict(x=positions[:, 0], y=positions[:, 1]))
        time.sleep(0.5)
