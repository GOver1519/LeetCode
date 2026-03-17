class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        min_len = len(strs[0])
        for word in strs:
            if len(word)<min_len:
                min_len = len(word)
        for j in range(min_len):
            ch = strs[0][j]

            for i in range(1, len(strs)):
                if strs[i][j] != ch:
                    return result
                    exit()
            result += ch
        return result