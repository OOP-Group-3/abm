import itertools
import numpy as np
from typing import Any, Dict, Iterable, Iterator, List, Optional, Set, Tuple, Union

from pandemicsim.agent import Agent

GridContent = Union[Optional[Agent], Set[Agent]]
FloatCoordinate = Union[Tuple[float, float], np.ndarray]

class ContinuousSpace:
	""" Continuous space where each agent can have an arbitrary position.

	Assumes that all agents are point objects, and have a pos property storing
	their position as an (x, y) tuple. This class uses a numpy array internally
	to store agent objects, to speed up neighborhood lookups.

	"""

	# _grid = None

	def __init__(self, width: float, height: float) -> None:
		""" Create a new continuous space."""

		self.width = width
		self.height = height

		self._agent_points = None	# type: np.ndarray of FloatCoordinates
		self._index_to_agent = {}  # type: Dict[int, Agent]
		self._agent_to_index = {}  # type: Dict[Agent, int]

	def place_agent(self, agent: Agent, pos: FloatCoordinate) -> None:
		""" Place a new agent in the space.

		Args:
			agent: Agent object to place.
			pos: Coordinate tuple for where to place the agent.

		"""
		if self._agent_points is None:
			self._agent_points = np.array([pos])
		else:
			self._agent_points = np.append(self._agent_points, np.array([pos]), axis=0)
		self._index_to_agent[self._agent_points.shape[0] - 1] = agent
		self._agent_to_index[agent] = self._agent_points.shape[0] - 1
		agent.pos = pos

	def move_agent(self, agent: Agent, pos: FloatCoordinate) -> None:
		""" Move an agent from its current position to a new position.

		Args:
			agent: The agent object to move.
			pos: Coordinate tuple to move the agent to.

		"""
		idx = self._agent_to_index[agent]
		self._agent_points[idx, 0] = pos[0]
		self._agent_points[idx, 1] = pos[1]
		agent.pos = pos

	def remove_agent(self, agent: Agent) -> None:
		""" Remove an agent from the simulation.

		Args:
			agent: The agent object to remove
			"""
		if agent not in self._agent_to_index:
			raise Exception("Agent does not exist in the space")
		idx = self._agent_to_index[agent]
		del self._agent_to_index[agent]
		max_idx = max(self._index_to_agent.keys())
		# Delete the agent's position and decrement the index/agent mapping
		self._agent_points = np.delete(self._agent_points, idx, axis=0)
		for a, index in self._agent_to_index.items():
			if index > idx:
				self._agent_to_index[a] = index - 1
				self._index_to_agent[index - 1] = a
		# The largest index is now redundant
		del self._index_to_agent[max_idx]
		agent.pos = None

	def get_neighbors(
		self, pos: FloatCoordinate, radius: float, include_center: bool = True
	) -> List[GridContent]:
		""" Get all objects within a certain radius.

		Args:
			pos: (x,y) coordinate tuple to center the search at.
			radius: Get all the objects within this distance of the center.
			include_center: If True, include an object at the *exact* provided
							coordinates. i.e. if you are searching for the
							neighbors of a given agent, True will include that
							agent in the results.

		"""
		deltas = np.abs(self._agent_points - np.array(pos))
		dists = deltas[:, 0] ** 2 + deltas[:, 1] ** 2

		(idxs,) = np.where(dists <= radius ** 2)
		neighbors = [
			self._index_to_agent[x] for x in idxs if include_center or dists[x] > 0
		]
		return neighbors

	def get_distance(self, pos_1: FloatCoordinate, pos_2: FloatCoordinate) -> float:
		""" Get the distance between two point, accounting for toroidal space.

		Args:
			pos_1, pos_2: Coordinate tuples for both points.

		"""
		x1, y1 = pos_1
		x2, y2 = pos_2

		dx = np.abs(x1 - x2)
		dy = np.abs(y1 - y2)

		return np.sqrt(dx * dx + dy * dy)

	def out_of_bounds(self, pos: FloatCoordinate) -> bool:
		""" Check if a point is out of bounds. """
		x, y = pos
		return x < self.x_min or x >= self.x_max or y < self.y_min or y >= self.y_max

	# def plot(self):
	# 	for point in self._agent_points:
	# 		plt.plot(point[0], point[1])
		