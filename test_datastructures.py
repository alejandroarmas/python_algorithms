import unittest
from datastructures import Heap, Graph

class TestGraph(unittest.TestCase):

	obj_1 = None

	def setUp(self) -> None:
		V = ["A", "B", "C", "D", "E", "F"]
		E = [["B", "C"], ["D", "E"], ["F"], [], ["F"], []]
		self.obj_1 = Graph(V, E)


	def test_init(self):
		self.assertEqual(self.obj_1.G["B"], ["D", "E"])


	def test_breadth_first_search(self):
		path_1 = self.obj_1.breadth_first_search("A")
		# {Node : Parent}
		expected_path_1 = {
			"A": None,
			"B": "A",
			"C": "A",
			"D": "B",
			"E": "B",
			"F": "C"
		}
		path_2 = self.obj_1.breadth_first_search("B")
		expected_path_2 = {
			"A": None,
			"B": None,
			"C": None,
			"D": "B",
			"E": "B",
			"F": "E"
		}
		path_3 = self.obj_1.breadth_first_search("F")
		expected_path_3 = {
			"A": None,
			"B": None,
			"C": None,
			"D": None,
			"E": None,
			"F": None
		}

		self.assertEqual(path_1, expected_path_1)
		self.assertEqual(path_2, expected_path_2)
		self.assertEqual(path_3, expected_path_3)

class TestHeap(unittest.TestCase):
	dat_1 = dat_2 = None


	# Method prepares the test fixture
	def setUp(self) -> None:
		list_1 = [1, 6, 2, 2, 23, 54, 43]
		list_2 = [1]
		list_3 = [5, 3, 2]
		self.dat_1 = Heap(list_1)
		self.dat_2 = Heap(list_2)
		self.dat_3 = Heap(list_3)


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


	def tearDown(self) -> None:
		self.dat_1 = None
		self.dat_2 = None


if __name__ == "__main__":
	unittest.main()
