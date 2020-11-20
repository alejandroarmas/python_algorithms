import unittest

from datastructures import Sort 

class TestSort(unittest.TestCase):

	def setUp(self):
		data_1 = [6, 3, 7, 2, 4, 6]
		data_2 = ["b", "d", "g", "a", "j", "c"]

		self.integer_array = Sort(data_1) 
		self.character_array = Sort(data_2)
		self.empty_array = Sort()
		self.single_item_array = Sort([2])

	def test_quicksort(self):
		sorted_integers = self.integer_array.quicksort()
		sorted_characters = self.character_array.quicksort()
		self.assertEqual(sorted_integers, [2, 3, 4, 6, 6, 7])
		self.assertEqual(sorted_characters, ["a", "b", "c", "d", "g", "j"])

	
	def test_quicksort_edge(self):
		sorted_empty = self.empty_array.quicksort()
		sorted_single_item = self.single_item_array.quicksort()
		self.assertEqual(sorted_empty, [])
		self.assertEqual(sorted_single_item, [2])


	def test_mergeSort(self):
			sorted_integers = self.integer_array.mergeSort()
			sorted_characters = self.character_array.mergeSort()
			self.assertEqual(sorted_integers, [2, 3, 4, 6, 6, 7])
			self.assertEqual(sorted_characters, ["a", "b", "c", "d", "g", "j"])

	
	def test_mergeSort_edge(self):
		sorted_empty = self.empty_array.mergeSort()
		sorted_single_item = self.single_item_array.mergeSort()
		self.assertEqual(sorted_empty, [])
		self.assertEqual(sorted_single_item, [2])
