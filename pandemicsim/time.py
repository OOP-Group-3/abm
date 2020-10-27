from collections import OrderedDict
from typing import Dict, Iterator, List, Optional, Union

from pandemicsim.agent import Agent
from pandemicsim.model import Model

class BaseScheduler:
    """ Simplest scheduler; activates agents one at a time, in the order
    they were added.

    Assumes that each agent added has a *step* method which takes no arguments.
    """

    def __init__(self, model: Model) -> None:
        """ Create a new, empty BaseScheduler. """
        self.model = model
        self.steps = 0
        self.time = 0  # type: TimeT
        self._agents = OrderedDict()  # type: Dict[int, Agent]

    def add(self, agent: Agent) -> None:
        """ Add an Agent object to the schedule.

        Args:
            agent: An Agent to be added to the schedule. NOTE: The agent must
            have a step() method.

        """
        self._agents[agent.unique_id] = agent

    def remove(self, agent: Agent) -> None:
        """ Remove all instances of a given agent from the schedule.

        Args:
            agent: An agent object.

        """
        del self._agents[agent.unique_id]

    def step(self) -> None:
        """ Execute the step of all the agents, one at a time. """
        print("Step: ", self.steps)
        for agent in self.agent_buffer(shuffled=False):
            agent.step()
            # debug
            print(agent.pos)
        self.steps += 1
        self.time += 1

    def get_agent_count(self) -> int:
        """ Returns the current number of agents in the queue. """
        return len(self._agents.keys())

    @property
    def agents(self) -> List[Agent]:
        return list(self._agents.values())

    def agent_buffer(self, shuffled: bool = False) -> Iterator[Agent]:
        """ Simple generator that yields the agents while letting the user
        remove and/or add agents during stepping.

        """
        agent_keys = list(self._agents.keys())
        if shuffled:
            self.model.random.shuffle(agent_keys)

        for key in agent_keys:
            if key in self._agents:
                yield self._agents[key]
