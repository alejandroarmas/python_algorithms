import copy


class Heap():

	def __init__(self, arr=None):
		'''
		This is done to avoid a persistent list in the mutable argument among all instances of this class.
		If you did not do this then all data would be shared.
		:param arr: array of values
		'''

		if arr == None:
			self.data = []
		else:
			self.data = copy.copy(arr)  # Shallow copy the list
			self.create_heap()


	def create_heap(self):
		'''
		Procedure that turns self.data list into a heap descending from largest to smallest.
		'''

		n = self.data.__len__()
		non_leaf_indexes = [x - 1 for x in range(n - 1, 0, -1) if x < n // 2 + 1]  # Create reversed list of the non-leaf indexes using list comprehension.

		for index in non_leaf_indexes:
			self.max_heapify(index)


	def max_heapify(self, index):
		'''
		Procedure, with iterative control structure, which provides heap property beginning at some index.
		:param index: Initialization location. While loop will keep looping until all children of index node follow heap property.
		'''
		n = self.data.__len__()

		flag = bool(n)  # True if arr contains an item

		while flag:
			#  Obtain value of parent node.
			val = self.data[index]

			# Obtain the values of the children leaf nodes.
			l_child_index = 2 * index + 1
			r_child_index = 2 * index + 2

			# Assign max_index to largest value in a 3-tuple of parent and leaf nodes.
			if l_child_index < n and self.data[l_child_index] > self.data[index]:
				max_child_index = l_child_index
			else:
				max_child_index = index
			if r_child_index < n and self.data[r_child_index] > self.data[max_child_index]:
				max_child_index = r_child_index

			temp_val = None  # Placeholder for swapping with parent node if needed.

			flag = max_child_index != index

			# If swap is performed, we repeat while loop until no longer. i.e. a child node is greater than parent.
			if flag:
				max_child_val = self.data[max_child_index]
				temp_val = val
				self.data[index] = max_child_val  # Assign parent node the value of the max child.
				self.data[max_child_index] = temp_val  # Assign the leaf node the value of the parent.
				index = max_child_index


	def remove(self, i=0):
		'''
		Takes about O(logn) time to heapify list once target value is extracted.
		Basic idea is to pop the value at index 0, replace it with last value and
		heapify list.
		:param i: index which is to be deleted from the heap.
		:return: value from the index popped out.
		'''

		temp = self.data[-1]
		self.data[-1] = self.data[i]
		self.data[i] = temp
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
		:return: An object that can be iterated open. i.e. it will return data one element at a time.
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
		sorted_list = []
		data = copy.copy(self.data)

		while self.data.__len__() != 0:
			sorted_list.append(self.remove(0))
		self.data = data
		return sorted_list


	@staticmethod
	def par_index(i):
		return i // 2 if i % 2 == 1 or i == 0 else i // 2 - 1


