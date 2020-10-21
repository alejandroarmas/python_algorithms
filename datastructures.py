import copy
from collections import deque, namedtuple
# Double Ended Queue Object for both stack
# and queue operations.
from priorityQueue import PriorityQueue
import numpy as np


class Heap():

	def __init__(self, arr=None):
		'''
		Conditional Statement is done to avoid a persistent list in the mutable
		argument among all instances of this class.
		If you did not do this then all data would be shared.
		:param arr: array of values
		'''

		if arr is None:
			self.data = []
		else:
			self.data = copy.deepcopy(arr)  # Deep copy the list
			self.create_heap()

	def create_heap(self):
		'''
		Procedure that turns self.data list into a heap descending from largest
		to smallest.
		'''

		n = self.data.__len__()
		# Create reversed list of the non-leaf indexes using list comprehension.
		non_leaf_indexes = [x - 1 for x in range(n - 1, 0, -1) if x < n // 2 + 1]

		for index in non_leaf_indexes:
			self.max_heapify(index)


	def max_heapify(self, index):
		'''
		Procedure, with iterative control structure, which provides heap property
		beginning at some index.
		:param index: Initialization location. While loop will keep looping until
		all children of index node follow heap property.
		'''
		n = self.data.__len__()

		flag = bool(n)  # True if arr contains an item

		while flag:
			#  Obtain value of parent node.
			val = self.data[index]

			# Obtain the values of the children leaf nodes.
			l_child_index = 2 * index + 1
			r_child_index = 2 * index + 2

			# Assign max_index to largest value in a 3-tuple of parent and leaf
			# nodes.
			if l_child_index < n and self.data[l_child_index] > self.data[index]:
				max_child_index = l_child_index
			else:
				max_child_index = index
			if r_child_index < n and self.data[r_child_index] > self.data[max_child_index]:
				max_child_index = r_child_index

			temp_val = None  # Placeholder for swapping with parent node if needed.

			flag = max_child_index != index

			# If swap is performed, we repeat while loop until no longer.
			# i.e. a child node is greater than parent.
			if flag:
				max_child_val = self.data[max_child_index]
				temp_val = val
				# Assign parent node the value of the max child.
				self.data[index] = max_child_val
				# Assign the leaf node the value of the parent.
				self.data[max_child_index] = temp_val
				index = max_child_index


	def remove(self, i=0):
		'''
		Takes about O(logn) time to heapify list once target value is extracted.
		Basic idea is to pop the value at index 0, replace it with last value and
		heapify list.
		:param i: index which is to be deleted from the heap.
		:return: value from the index popped out.
		'''

		self.data[-1], self.data[i] = self.data[i], self.data[-1]
		val = self.data.pop(-1)
		self.max_heapify(i)
		return val


	def add(self, val):
		'''
		Add a singular value to the Heap.
		:param val: Value to be added.
		:return: self.data is updated to reflect addition of val.
		'''
		i = self.data.__len__()
		self.data.append(val)

		nodes_to_inspect = [self.par_index(i)]

		while nodes_to_inspect[-1] != 0:
			nodes_to_inspect.append(self.par_index(nodes_to_inspect[-1]))

		for node in nodes_to_inspect:
			self.max_heapify(node)

	def __iter__(self):
		'''
		This dunder method enables Heap to return an Iterator.
		:return: An object that can be iterated open.
		i.e. it will return data one element at a time.
		'''
		self.n = 0
		return self

	def __next__(self):
		'''
		:return: The next item for iteration.
		'''
		if self.n < self.data.__len__():
			result = self.data[self.n]
			self.n += 1
			return result
		else:
			raise StopIteration

	def __len__(self):
		return self.data.__len__()

	def heapsort(self):
		'''
		:return: Sorted Copy of all the items in heap
		'''
		sorted_list = []
		data = copy.deepcopy(self.data)

		while self.data.__len__() != 0:
			sorted_list.append(self.remove(0))
		self.data = data
		return sorted_list

	@staticmethod
	def par_index(i):
		return i // 2 if i % 2 == 1 or i == 0 else i // 2 - 1


class Graph():

	def __init__(self, V, E, W = None):
		# Adjacency List representation
		Node = namedtuple("Node", ["vertex", "edgeWeight"])

		# If no weights were assigned, then list all as 1.
		if W is None:
			edges = ([Node(v, 1) for v in vs] for vs in E)
		else:
			edges = ([Node(v, w) for v, w in zip(vs, ws)] for vs, ws in zip(E, W))
		self.G = dict(zip(V, edges))
		# Create our Graph

	# G = {v: e for v, e in zip(V, E)}
	# Use this to generate Graph of our Vertix and Edges only when you
	# want to filter based on keys or values

	def breadth_first_search(self, init_vertex: str = None) -> "List of Search order":
		'''
		Efficient algorithm for level-order searching through a graph.
		- Time complexity: O(log(n + m)) where n is # of nodes and m is # of edges.
		- Space complexity: O(log(n)) where n is the # of nodes that need to be "discovered".

		:param Char. init_vertix: Vertex to begin the search at.

		Idea:

		1. Add a node to the queue
		2. Remove node
		3. Retrieve unvisited neighbors of the removed node, add them to queue
		4. Repeat steps 1, 2, and 3 as long as the queue is not empty.

		Notes:
		- Works on directed and undirected graph.
		- Since a tree is a connected acyclic graph with n nodes, this algorithm is
		 typically used for level-order traversal.
		- There can only be n - 1 edges, therefore time complexity can only be O(log(n)).
		- In-order traversal level by level then [left right] in binary list will
		involve exploring root node, then left tree then right tree.

		'''

		vertices = list(self.G.keys())  # Extract the list of vertices
		num_vertices = vertices.__len__()
		# Initialize list of tuples denoting all vertices are yet to be found.
		discovered = dict(zip(vertices, [False] * num_vertices))
		# Initialize list of tuples denoting all vertices parents in new search tree.
		# parent = dict(zip(vertices, [None] * num_vertices))
		order = []

		queue = deque(maxlen=num_vertices)  # Treat our double-ended queue as a queue

		# Begin from a random Vertex
		rand_index = np.random.randint(0, num_vertices - 1)
		init_vertex = vertices[rand_index] if init_vertex is None else init_vertex.upper()
		discovered[init_vertex] = True
		# Enqueue the initial vertex.
		queue.append(init_vertex)
		while queue:
			# While the queue is not empty we explore the first queued node.
			curr_node = queue.popleft()  # Dequeue the current vertex <- "Explored" i.e. we do stuff with current node.
			# print(f"Processed {curr_node}!")  # This is the space in your algorithm where you do stuff.
			order.append(curr_node)  # Only used for unittesting correctness.
			for incident_vertex in self.G[curr_node]:
				# for each current node, you will add all incident nodes to the queue if they have not been discovered.
				if not discovered[incident_vertex.vertex]:
					discovered[incident_vertex.vertex] = True
					# parent[incident_vertex] = curr_node
					queue.append(incident_vertex.vertex)
		return order

	def depth_first_search(self, init_vertex: str = None) -> "List of search order":
		'''
		Efficient algorithm for post-order traversal through a graph.
		- Time complexity: O(log(n + m)) where n is # of nodes and m is # of edges.
		- Space complexity: O(log(n)) where n is the # of nodes that need to be "explored".

		:param Char. init_vertix: Vertex to begin the search at.

		Idea:

		1. Add a node to the stack
		2. Remove node
		3. Retrieve unexplored neighbors of the removed node, add them to stack
		4. Repeat steps 1, 2, and 3 as long as the stack is not empty.

		Notes:
		For Binary Search Trees:
		- Pre-order traversal [current left right] in binary list will involve exploring
		 root node, then left tree then right tree.
		- In-order traversal [left current right]
		- Post-order traversal [left right current]
		'''
		vertices = list(self.G.keys())  # Extract the list of vertices
		num_vertices = vertices.__len__()
		# Initialize list of tuples denoting all vertices are yet to be found.
		explored = dict(zip(vertices, [False] * num_vertices))
		# Initialize list of tuples denoting all vertices parents in new search tree.
		# parent = dict(zip(vertices, [None] * num_vertices))
		order = []

		stack = deque(maxlen=num_vertices)  # Treat our double-ended queue as a stack

		# Begin from a random Vertex
		rand_index = np.random.randint(0, num_vertices - 1)
		init_vertex = vertices[rand_index] if init_vertex is None else init_vertex.upper()
		# Add first vertex
		stack.append(init_vertex)
		while stack:  # While the stack is not empty we explore latest node added
			curr_node = stack.pop()
			order.append(curr_node)
			if not explored[curr_node]:
				# This is the space in your algorithm where you do stuff.
				# print(f"Processed {curr_node}!")
				explored[curr_node] = True

				# Order of items placed on stack dictated by V order.
				for incident_node in self.G[curr_node]:
					if not explored[incident_node.vertex]:
						# parent[incident_node] = curr_node
						stack.append(incident_node.vertex)
		return order


	def dijkstra(self, init_vert):
		'''
		Used for solving the shortest path problem on
		graph with nonnegative weight for each edge.
		i.e. finding a path between two nodes
		s.t. sum of constituent weights is minimized.
		Greedy algorithm because it nearsightedly always
		chooses to relax the shorted-path tree.
		:return Dictionary Tuple where target_dist is shortest-path tree
		and parent is dictionary assigning node inheritance
		'''

		parent = {}
		# Populate target distance dictionary with infinities
		# Except for the initial vertex.
		target_dist = {vert: float("inf") for vert in self.G.keys()
		               if vert != init_vert}
		target_dist[init_vert] = 0
		dist_queue = PriorityQueue()

		# Populate priority queue with node and distance pairs.
		for vert in target_dist.keys():
			dist_queue.add(vert, target_dist[vert])  # (distance, vertex)

		while dist_queue:
			curr = dist_queue.pop()
			for incident_node in self.G[curr.task]:
				if curr.priority + incident_node.edgeWeight < target_dist[incident_node.vertex]:
					target_dist[incident_node.vertex] = curr.priority + incident_node.edgeWeight
					# Perform Relaxation on target distance dictionary
					# if we can find a shorter path from init_vert to target.
					dist_queue.add(incident_node.vertex, target_dist[incident_node.vertex])
					# Add the current node as the parent, for future pathing.
					parent[incident_node.vertex] = curr.task

		return {"target_dist": target_dist, "parent": parent}


	# def prims(self):
	# 	"""
	# 	Find a minimum spanning tree T of an undirected, positively
	# 	weighted, connected graph G. Returns a tree T which contains
	# 	all original vertices V, but subset of edges.
	# 	Greedy algorithm because it nearsightedly selects
	# 	lowest edge weight
	# 	:return:
	# 	"""
	# 	vertices = copy.deepcopy(self.G.keys())
	# 	pass

