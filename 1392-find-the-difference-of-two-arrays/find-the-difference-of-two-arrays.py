class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer1 = []
        answer2 = []
        for i in nums1:
            if i not in nums2 and i not in answer1:
                answer1.append(i)
        for i in nums2:
            if i not in nums1 and i not in answer2:
                answer2.append(i)
        return answer1, answer2