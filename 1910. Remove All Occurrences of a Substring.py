class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result = s.partition(part)
        while result[1]:
            result = result[0]+result[2]
            result = result.partition(part)
        return result[0]
    
