from pandemicsim.model import Model
from random import Random

class Agent:
	""" Base class for a model agent. """

	def __init__(self, unique_id: int = None, model: Model = None) -> None:
		""" Create a new agent. """
		self.unique_id = unique_id
		self.model = model
		self.pos = None

	def step(self) -> None:
		""" A single step of the agent. """
		pass

	# TODO: what does advance do that step() doesn't?
	def advance(self) -> None:
		pass

	# TODO: what is this for?
	@property
	def random(self) -> Random:
		return self.model.random