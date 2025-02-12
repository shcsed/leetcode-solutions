class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for elements in zip(*strs):
            if len(set(elements)) == 1:
                lcp += elements[0]
            else:
                break
        return lcp
