import unittest

from datastructures import Heap

class TestHeap(unittest.TestCase):
	
	data_we_want_sorted = single_item_heap = None


	# Method prepares the test fixture
	def setUp(self) -> None:
		list_1 = [1, 6, 2, 2, 23, 54, 43]
		list_2 = [1]
		list_3 = [5, 3, 2]

		self.data_we_want_sorted = Heap(list_1)
		self.single_item_heap = Heap(list_2)
		self.three_item_heap = Heap(list_3)


	def test_parent(self):
		self.assertEqual(0, Heap.par_index(1))
		self.assertEqual(1, Heap.par_index(3))
		self.assertEqual(0, Heap.par_index(0))
		self.assertEqual(2, Heap.par_index(5))
		self.assertEqual(2, Heap.par_index(6))


	def test_add(self):
		self.three_item_heap.add(1)
		self.assertEqual(len(self.three_item_heap), 4)
		self.assertEqual(self.three_item_heap.data, [5, 3, 2, 1])


	def test_remove(self):
		self.single_item_heap.remove()
		self.three_item_heap.remove(-1)
		self.assertEqual(self.single_item_heap.data, [])
		self.assertEqual(self.three_item_heap.data, [5, 3])


	def test_max_heapify(self):
		self.single_item_heap.max_heapify(0)
		self.assertEqual(self.single_item_heap.data, [1])
		self.single_item_heap.add(2)
		self.assertEqual(self.single_item_heap.data, [2, 1])


	def test_sort(self):
		sorted_data = [54, 43, 23, 6, 2, 2, 1]

		self.assertEqual(self.data_we_want_sorted.heapsort(), sorted_data)
		self.assertEqual(self.single_item_heap.heapsort(), [1])


	def tearDown(self) -> None:
		self.data_we_want_sorted = self.three_item_heap = self.single_item_heap = None

