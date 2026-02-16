class Solution(object):
    def check(self, nums):
        if nums == sorted(nums):
            return True
        else:
            for i in range(len(nums)):
                nums = nums[1:] + nums[0:1]
                if nums == sorted(nums):
                    return True
        return False
        