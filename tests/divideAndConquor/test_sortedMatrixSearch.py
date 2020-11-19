import unittest 

from divideAndConquor import sortedMatrixSearch


class TestSortedMatrixSearch(unittest.TestCase):
    

    def setUp(self):
        
        self.sortedMatrix = [
            [1, 3, 5, 6, 7],
            [4, 5, 7, 8, 9],
            [5, 6, 8, 8, 11],
            [6, 7, 9, 9, 11],
            [8, 8, 9, 10, 12]
            ]
        
        self.emptyMatrix = []


    def test_retrieveTargetCoordinates(self):

        targetOneValue = 7
        targetTwoValue = 12
        targetThreeValue = 1
        
        targetOneCoordinates = (0, 4)
        targetTwoCoordinates = (4, 4)
        targetThreeCoordinates = (0, 0)

        expectedTargetOneCoordinates = sortedMatrixSearch(self.sortedMatrix, targetOneValue)
        expectedTargetTwoCoordinates = sortedMatrixSearch(self.sortedMatrix, targetTwoValue)
        expectedTargetThreeCoordinates = sortedMatrixSearch(self.sortedMatrix, targetThreeValue)
        
        self.assertEqual(expectedTargetOneCoordinates, targetOneCoordinates)
        self.assertEqual(expectedTargetTwoCoordinates, targetTwoCoordinates)
        self.assertEqual(expectedTargetThreeCoordinates, targetThreeCoordinates)


    def test_RetrieveItemNotInArray(self):

        targetValue = 420
        
        errorHandling = (-1, -1) 

        expectedTargetCoordinates = sortedMatrixSearch(self.sortedMatrix, targetValue)
        
        self.assertEqual(expectedTargetCoordinates, errorHandling)


    def test_EmptyMatrixHandling(self):

        targetValue = 420

        errorHandling = (-1, -1) 

        expectedTargetCoordinates = sortedMatrixSearch(self.emptyMatrix, targetValue)
        
        self.assertEqual(expectedTargetCoordinates, errorHandling)


