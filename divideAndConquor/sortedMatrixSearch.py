
def sortedMatrixSearch(array, target):
    """
    Matrix variant where the rows are sorted and columns are sorted.

    Start at top right corner and prune our search space by:
        - A single row if our target is greater than where we land
        - A single column if our target is lesser than where we land
        O(n + m)
    """

    numRows = len(array)
    numColumns = len(array[0]) if numRows > 0 else 0 

    currentRowIndex, currentColumnIndex = 0, numColumns - 1

    foundTarget = False
    returnIndexes = (-1, -1) 

    while currentRowIndex < numRows and currentColumnIndex >= 0 and not foundTarget:
        
        if array[currentRowIndex][currentColumnIndex] == target:
            returnIndexes = (currentRowIndex, currentColumnIndex)
            foundTarget = True 

        elif array[currentRowIndex][currentColumnIndex] > target:
            currentColumnIndex -= 1

        elif array[currentRowIndex][currentColumnIndex] < target:
            currentRowIndex += 1

    return returnIndexes
