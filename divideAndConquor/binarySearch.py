
from datastructures import Sort 

def binarySearch(array, target):
    """
    Decision to cut search space in half based on greater or less than operation.
    O(n) time complexity 
    """
    
    leftBoundSearchSpace, rightBoundSearchSpace = 0, len(array) - 1

    foundTarget = False
    index = -1 

    while leftBoundSearchSpace < rightBoundSearchSpace and not foundTarget:

        midPoint = (leftBoundSearchSpace + rightBoundSearchSpace) // 2

        if array[midPoint] == target:
            index = midPoint
            foundTarget = True


        elif array[midPoint] > target:
            rightBoundSearchSpace = midPoint - 1
        

        else:
            leftBoundSearchSpace = midPoint + 1 
    
    return index 
