import unittest
from datastructalgo import Heap


class TestHeap(unittest.TestCase):
	dat_1 = dat_2 = None


	# Method prepares the test fixture
	def setUp(self):
		list_1 = [1, 6, 2, 2, 23, 54, 43]
		list_2 = [1]
		list_3 = [5, 3, 2]
		self.dat_1 = Heap(list_1)
		self.dat_2 = Heap(list_2)
		self.dat_3 = Heap(list_3)
		print("Set up")


	def test_parent(self):
		self.assertEqual(0, Heap.par_index(1))
		self.assertEqual(1, Heap.par_index(3))
		self.assertEqual(0, Heap.par_index(0))
		self.assertEqual(2, Heap.par_index(5))
		self.assertEqual(2, Heap.par_index(6))


	def test_add(self):
		self.dat_3.add(1)
		self.assertEqual(len(self.dat_3), 4)
		self.assertEqual(self.dat_3.data, [5, 3, 2, 1])


	def test_remove(self):
		self.dat_2.remove()
		self.dat_3.remove(-1)
		self.assertEqual(self.dat_2.data, [])
		self.assertEqual(self.dat_3.data, [5, 3])


	def test_max_heapify(self):
		self.dat_2.max_heapify(0)
		self.assertEqual(self.dat_2.data, [1])
		self.dat_2.add(2)
		self.assertEqual(self.dat_2.data, [2, 1])


	def test_sort(self):
		self.assertEqual(self.dat_1.heapsort(), [54, 43, 23, 6, 2, 2, 1])
		self.assertEqual(self.dat_2.heapsort(), [1])


	def tearDown(self):
		self.dat_1 = None
		self.dat_2 = None


if __name__ == "__main__":
	unittest.main()
