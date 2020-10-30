import copy 


class Sort():

	"""
	Different Implementations of Sorting Algorithms.
	"""

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
		


	def quicksort(self):
		"""
		Wrapper function for quicksort algorithm.

		:return: returns a sorted copy of self.data. 
		"""
		low = 0  # Low 
		high = self.data.__len__() - 1  # Act as an index right after list ends.
		data = copy.deepcopy(self.data)  # Copy data 
			
		self.__quicksort(data, low, high)
		return data
		

	@staticmethod	
	def __quicksort(arr, low, high):
		"""
		Divide and Conquor strategy that works on the principle of 
		sorted position w/ Hoare Partitioning scheme. 
		i.e. item is in sorted position if all items before are lesser and items after are greater.
		
		Approach:
		1. Select a pivot data point in __partition method.
		2. Move all the data points lesser than pivot value below pivot position and 
			greater points above the pivot position in __partition method.
		3. Recursively call algorithm in __quicksort method on areas below and 
			above the pivot position.
		"""
		if low < high:
				index = Sort.__partition(arr, low, high)
				Sort.__quicksort(arr=arr, low=low, high=index)
				Sort.__quicksort(arr=arr, low=index + 1, high=high)
		

	@staticmethod
	def __partition(data, low, high):
		"""
		Private member function used by quicksort algorithm to place first item into sorted position.
		"""

		# If data is randomly distributed, then selecting first item is
		# equivalent to random selection.
		pivot = data[low]

		while True:
			# Increment i index until it finds value greater than pivot
			while data[low] < pivot:
				low += 1
			# Deincrement j index until it finds value lesser than pivot
			while data[high] > pivot:
				high -= 1
			# If low has not crossed high index, perform tuple swap operation
			# else if there has been a cross, then return high index as partitioning position.
			if low >= high:
				return high 
			data[low], data[high] = data[high], data[low]
			low += 1
			high -= 1
			