class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        unpack = 0
        for i in digits:
            unpack = unpack*10+i
        add = unpack+1
        increment = list(map(int, str(add)))
        return increment        