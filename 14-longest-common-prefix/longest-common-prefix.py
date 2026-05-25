class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # Edge case: empty list
        if not strs:
            return ""
        
        first = strs[0]
        prefix = ""

        # Generate prefixes one by one
        for i in range(len(first)):
            
            current_prefix = first[:i + 1]

            # Check if all strings start with current_prefix
            for word in strs:
                if not word.startswith(current_prefix):
                    return prefix

            # Update valid prefix
            prefix = current_prefix

        return prefix
