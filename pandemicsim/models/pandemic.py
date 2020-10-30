from pandemicsim.models.base import Model
from pandemicsim.space import ContinuousSpace
from pandemicsim.time import BaseScheduler
from pandemicsim.agents.agents import Person
from pandemicsim.plot.bokeh import BokehPlotter


class Pandemic(Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = 150
        self.height = 100
        self.space = ContinuousSpace(self.width, self.height) if self.space is None else self.space
        self.schedule = BaseScheduler(self) if self.schedule is None else self.schedule
        self.initial_people = 5

        # initialise people only
        for _ in range(self.initial_people):
            x = self.random.randrange(self.space.width)
            y = self.random.randrange(self.space.height)
            person = Person(self.next_id(), (x, y), self)
            self.schedule.add(person)
            self.space.place_agent(person, (x, y))

        self.plotter = BokehPlotter(self.space)

    def next_id(self) -> int:
        """" Return the next unique ID for agents, increment current_id"""
        self.current_id += 1
        return self.current_id

    def step(self):
        self.schedule.step()

    def run_model(self, session, step_count=5):
        for _ in range(step_count):
            self.plotter.plot()
            self.step()
        session.show(self.plotter.fig)
