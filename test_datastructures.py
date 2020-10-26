import unittest
from datastructures import Heap, Graph


class TestGraph(unittest.TestCase):

	obj_1 = None

	def setUp(self) -> None:
		# Test a non-weighted graph for traversal algorithms
		V_1 = ["A", "B", "C", "D", "E", "F"]
		V_2 = ["A", "B", "C", "D", "E", "F"]
		E_1 = [
			["B", "C"],
			["D", "E"],
			["F"],
			[],
			["F"],
			[]
		]

		W_2 = [
			[1, 2],
			[1, 1],
			[2],
			[],
			[1],
			[]
		]
		self.obj_1 = Graph(V_1, E_1)
		self.obj_2 = Graph(V_2, E_1, W_2)

	def test_init(self):
		self.assertEqual(self.obj_1.G["B"], [("D", 1), ("E", 1)])


	def test_breadth_first_levelorder_search(self):
		# Level-Order Search.

		path_1 = self.obj_1.breadth_first_search("A")
		path_2 = self.obj_1.breadth_first_search("B")
		path_3 = self.obj_1.breadth_first_search("F")

		expected_path_1 = ["A", "B", "C", "D", "E", "F"]
		expected_path_2 = ["B", "D", "E", "F"]
		expected_path_3 = ["F"]

		self.assertEqual(path_1, expected_path_1)
		self.assertEqual(path_2, expected_path_2)
		self.assertEqual(path_3, expected_path_3)


	def test_depth_first_postorder_search(self):
		# Post-order Search.

		path_1 = self.obj_1.depth_first_search("A")
		path_2 = self.obj_1.depth_first_search("B")
		path_3 = self.obj_1.depth_first_search("F")

		expected_path_1 = ["A", "C", "F", "B", "E", "D"]
		expected_path_2 = ["B", "E", "F", "D"]
		expected_path_3 = ["F"]

		self.assertEqual(path_1, expected_path_1)
		self.assertEqual(path_2, expected_path_2)
		self.assertEqual(path_3, expected_path_3)


	def test_dijkstra(self):
		# Test Weighted Graph
		self.assertEqual(self.obj_2.dijkstra("A")["target_dist"]["F"], 3)
		# Test unWeighted Graph
		self.assertEqual(self.obj_1.dijkstra("A")["target_dist"]["F"], 2)


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
