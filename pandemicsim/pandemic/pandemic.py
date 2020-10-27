from pandemicsim.model import Model
from pandemicsim.space import ContinuousSpace
from pandemicsim.time import BaseScheduler
from pandemicsim.pandemic.agents import Person
import numpy as numpy

class Pandemic(Model):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.width = 150
		self.height = 100
		self.space = ContinuousSpace(self.width, self.height)
		self.schedule = BaseScheduler(self)
		self.initial_people = 5

		# initialise people only
		for i in range(self.initial_people):
			x = self.random.randrange(self.width)
			y = self.random.randrange(self.height)
			person = Person(self.next_id(), (x, y), self)
			self.schedule.add(person)
			self.space.place_agent(person, (x, y))
	
	def next_id(self) -> int:
		"""" Return the next unique ID for agents, increment current_id"""
		self.current_id += 1
		return self.current_id

	def step(self):
		self.schedule.step()

	def run_model(self, step_count = 20):
		for i in range(step_count):
			self.step()
		

