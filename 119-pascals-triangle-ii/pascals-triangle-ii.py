class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        output = []
        row = [1]
        for i in range(100):
            output.append(row)
            padded = [0] + row + [0]
            new_row = []
            for j in range(len(padded) - 1):
                new_row.append(padded[j] + padded[j+1])
            row = new_row
        return output[rowIndex]