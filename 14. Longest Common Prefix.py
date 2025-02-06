class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        i=0
        while i<len(min(strs)):
            letter = strs[0][i]
            for word in strs:
                if word[i] != letter:
                    return result
            i+=1
            result += letter
        return result
            
            
