class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = 1
        prefix_distinct = []
        sufix_distinct = []
        output = []
        for i in nums:
            prefix_distinct = nums[:prefix]
            sufix_distinct = nums[prefix:]
            output.append(len(set(prefix_distinct))-len(set(sufix_distinct)))
            prefix += 1
        return output
        