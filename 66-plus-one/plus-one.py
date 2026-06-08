class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ''.join(map(str, digits))
        result = int(string) + 1
        nums = []
        while result > 0:
            digit = result % 10
            nums.append(digit)
            result = result // 10
        nums.reverse()
        return nums