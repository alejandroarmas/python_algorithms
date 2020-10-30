import unittest
from datastructures import Heap, Graph, Sort


class TestGraph(unittest.TestCase):

	directed_graph = directed_weighted_graph = None
	

	def setUp(self) -> None:

		vertix_set = ["A", "B", "C", "D", "E", "F"]
		edge_set = [
			["B", "C"],
			["D", "E"],
			["F"],
			[],
			["F"],
			[]
		]

		weights = [
			[1, 2],
			[1, 1],
			[2],
			[],
			[1],
			[]
		]

		self.directed_graph = Graph(vertix_set, edge_set)
		self.directed_weighted_graph = Graph(vertix_set, edge_set, weights)

	def test_init(self):
		self.assertEqual(self.directed_graph.G["B"], [("D", 1), ("E", 1)])


	def test_breadth_first_levelorder_search(self):
		path_beginning_vertex_a = self.directed_graph.breadth_first_search("A")
		expected_path_beginning_vertex_a = ["A", "B", "C", "D", "E", "F"]

		self.assertEqual(
			path_beginning_vertex_a,
			 expected_path_beginning_vertex_a)


	def test_breadth_first_levelorder_search_center_vertex(self):
		path_beginning_vertex_middle = self.directed_graph.breadth_first_search("B")
		expected_path_beginning_vertex_middle = ["B", "D", "E", "F"]

		self.assertEqual(
			path_beginning_vertex_middle,
			 expected_path_beginning_vertex_middle)

	
	def test_breadth_first_levelorder_search_no_outbound(self):
		path_beginning_vertex_no_outbound = self.directed_graph.breadth_first_search("F")
		expected_path_beginning_vertex_no_outbound = ["F"]

		self.assertEqual(
			path_beginning_vertex_no_outbound,
			 expected_path_beginning_vertex_no_outbound)


	def test_depth_first_postorder_search(self):
		path_beginning_vertex_a = self.directed_graph.depth_first_search("A")
		expected_path_beginning_vertex_a = ["A", "C", "F", "B", "E", "D"]
		
		self.assertEqual(path_beginning_vertex_a, expected_path_beginning_vertex_a)


	def test_depth_first_postorder_search_center_vertex(self):
		path_beginning_vertex_middle = self.directed_graph.depth_first_search("B")
		expected_path_beginning_vertex_middle = ["B", "E", "F", "D"]
		
		self.assertEqual(path_beginning_vertex_middle,
		 expected_path_beginning_vertex_middle)


	def test_depth_first_postorder_search_no_outbound(self):
		path_beginning_vertex_no_outbound = self.directed_graph.depth_first_search("F")
		expected_path_beginning_vertex_no_outbound = ["F"]
		
		self.assertEqual(path_beginning_vertex_no_outbound,
		 expected_path_beginning_vertex_no_outbound)


	def test_dijkstra(self):
		init_vertex = "A"
		target_vertex = "F"
		# Test Weighted Graph
		self.assertEqual(
			self.directed_weighted_graph.dijkstra(init_vertex)
			["target_dist"][target_vertex], 3)
		# Test unWeighted Graph
		self.assertEqual(
			self.directed_graph.dijkstra(init_vertex)
			["target_dist"][target_vertex], 2)


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


class TestSort(unittest.TestCase):

	def setUp(self):
		data_1 = [6, 3, 7, 2, 4, 6]
		data_2 = ["b", "d", "g", "a", "j", "c"]

		self.sortObj1 = Sort(data_1) 
		self.sortObj2 = Sort(data_2)
		self.sortObj3 = Sort()
		self.sortObj4 = Sort([2])

	def test_quicksort(self):
		sorted_list_1 = self.sortObj1.quicksort()
		sorted_list_2 = self.sortObj2.quicksort()
		self.assertEqual(sorted_list_1, [2, 3, 4, 6, 6, 7])
		self.assertEqual(sorted_list_2, ["a", "b", "c", "d", "g", "j"])

	
	def test_quicksort_edge(self):
		sorted_list_3 = self.sortObj3.quicksort()
		sorted_list_4 = self.sortObj4.quicksort()
		self.assertEqual(sorted_list_3, [])
		self.assertEqual(sorted_list_4, [2])
		


if __name__ == "__main__":
	unittest.main()
