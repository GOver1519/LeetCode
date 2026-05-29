class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        replace = len(nums) -1
        i = 0
        while i <= replace:
            if nums[i] == val:
                nums[i], nums[replace] = nums[replace], nums[i]
                replace -= 1
            else:
                count += 1
                i += 1
        return count