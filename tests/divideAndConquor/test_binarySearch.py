import unittest 

from divideAndConquor import binarySearch


class TestBinarySearch(unittest.TestCase):


    def setUp(self) -> None:

        self.regularArray = [1, 4, 9, 14, 40]
        self.emptyArray = []
        self.repeatItemsArray = [3, 5, 7, 9, 9, 9, 9, 12]

    
    def test_TargetRetrieval(self):
        
        targetOne = 14
        targetTwo = 9
        targetOneIndex = 3
        targetTwoIndex = 2

        returnedIndexOne = binarySearch(self.regularArray, targetOne)
        returnedIndexTwo = binarySearch(self.regularArray, targetTwo)

        self.assertEqual(targetOneIndex, returnedIndexOne)        
        self.assertEqual(targetTwoIndex, returnedIndexTwo)


    def test_EmptySearch(self):

        target = 420
        expectedErrorReturn = -1

        returnedIndex = binarySearch(self.emptyArray, target)

        self.assertEqual(returnedIndex, expectedErrorReturn) 
        
    
    def test_TargetNotInArray(self):
        target = 54   
        expectedErrorReturn = -1

        returnedIndex = binarySearch(self.regularArray, target)
        
        self.assertEqual(returnedIndex, expectedErrorReturn) 
        

    def test_RepeatedIndexHandling(self):

        repeatedTarget = 9
        # We would expect the 3rd index to be looked at first in a 7 item array
         
        targetIndex = 3

        returnedIndex = binarySearch(self.repeatItemsArray, repeatedTarget)
        self.assertEqual(returnedIndex, targetIndex)
