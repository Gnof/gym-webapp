import os, subprocess, time, signal
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding

import logging
logger = logging.getLogger(__name__)

class Webapp(gym.Env, utils.EzPickle):
	metadata = {'render.modes': ['human']}

	def __init__(self):
		self.viewer = None
        self.server_process = None
        self.server_port = None

        self._configure_environment()

    def _configure_environment(self):
        """
        Provides a chance for subclasses to override this method and supply
        a different server configuration. By default, we initialize one
        offense agent against no defenders.
        """
        logger.debug("Configuring Environment")

     def _step(self, action):
        self._take_action(action)
        self.status = self.env.step()
        reward = self._get_reward()
        ob = self.env.getState()
        
        return ob, reward, True, {}

    def _take_action(self, action):
        """ Take an action within a browser environment """
        logger.debug("Take action: %s" % action)
        

    def _get_reward(self):
        """ Reward is given for finding an end state """
        return 1

    def _reset(self):
        """ Create a new browser and start over """
        
        return self.env.getState()

    def _render(self, mode='human', close=False):
        """ Viewer only supports human mode currently. """
        if close:
            if self.viewer is not None:
                os.kill(self.viewer.pid, signal.SIGKILL)
        else:
            if self.viewer is None:
                self._start_viewer()