class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string_merged = ""
        for i in word1:
            for j in word2:
                string_merged += i
                string_merged += j

        return string_merged