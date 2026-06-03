class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = nums
        for i in range(len(a)):
            if target in a:
                return a.index(target)
        nums.append(target)
        nums.sort()

        return nums.index(target)
                
                