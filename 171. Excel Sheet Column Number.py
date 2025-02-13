class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result*=26
            result+= ord(char)-64
        return result
        
