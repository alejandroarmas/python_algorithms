import copy
from collections import namedtuple
import heapq
import itertools


# Code taken from https://docs.python.org/3.5/library/heapq.html#priority-queue-implementation-notes
class PriorityQueue():

	REMOVED = '<removed-task>'  # placeholder for a removed task

	def __init__(self, arr=None):
		'''
		Conditional Statement is done to avoid a persistent list in the 
		mutable argument among all instances of this class.
		If you did not do this then all data would be shared.
		:param arr: array of values
		'''
		if arr is None:
			self.data = []
		else:
			self.data = []  # Deep copy the list and perform heapify.
			heapq.heapify(self.data)

		self.entry_finder = {}  # mapping of tasks to entries
		self.counter = itertools.count()  # unique sequence count


	def add(self, task, priority=0):
		"""
		Add a new task or update the priority of an existing task.
		If updating task,
		"""
		if task in self.entry_finder:
			self.remove(task)
		count = next(self.counter)  # Increments count each time item is added ( Saves index ).
		entry = [priority, count, task]
		self.entry_finder[task] = entry
		heapq.heappush(self.data, entry)


	def remove(self, task):
		"""Mark an existing task as REMOVED.  Raise KeyError if not found."""
		entry = self.entry_finder.pop(task)
		entry[-1] = self.REMOVED


	def pop(self):
		"""Remove and return the lowest priority task. Raise KeyError if empty."""
		while self.data:
			priority, count, task = heapq.heappop(self.data)
			Node = namedtuple("Node", ["priority", "task"])
			if task is not self.REMOVED:
				del self.entry_finder[task]
				return Node(priority, task)
		raise KeyError('pop from an empty priority queue')


	def __bool__(self):
		return self.data and self.data[0][2] != self.REMOVED



