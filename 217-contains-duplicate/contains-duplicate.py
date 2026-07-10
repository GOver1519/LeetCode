class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique = set(nums)
        if len(nums) == len(unique):
            return False
        else:
            return True