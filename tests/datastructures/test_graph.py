import unittest 

from datastructures import Graph


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

