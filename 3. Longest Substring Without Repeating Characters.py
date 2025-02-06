class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s): return 0
        unique=[1]
        for i in range(len(s)):
            uniqueChar = set(s[i])
            for j in range(i+1,len(s)):
                if s[j] in uniqueChar:
                    unique.append(j-i)
                    break
                uniqueChar.add(s[j])
            else: 
                unique.append(len(s)-i)
        return max(unique)
                    
