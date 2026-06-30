# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def helper(lower_bound, upper_bound):
            if lower_bound > upper_bound:
                return None
            mid = (lower_bound + upper_bound) // 2
            root = TreeNode(nums[mid])
            root.left = helper(lower_bound, mid -1)
            root.right = helper(mid+1, upper_bound)
            return root
        return helper(0, len(nums) - 1)
        