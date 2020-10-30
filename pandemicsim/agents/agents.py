from pandemicsim.agents.base import Agent
import numpy as np


class Person(Agent):
    def __init__(self, unique_id, pos, model=None):
        super().__init__(unique_id, model)
        self.pos = pos  # np.array(float32)
        self.mobility = 1

    def random_move(self):
        self.pos += self.mobility * np.random.rand(2)
        self.model.space.move_agent(self, self.pos)

    def step(self):
        self.random_move()
