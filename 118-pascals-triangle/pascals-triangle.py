class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        sample = [1]

        for i in range(numRows):
            output.append(sample)

            padded = [0]+sample+[0]
            new_row = []

            for j in range(len(padded)-1):
                new_row.append(padded[j] + padded[j + 1])
            sample = new_row
        return output
        