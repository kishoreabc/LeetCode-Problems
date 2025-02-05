class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber>0:
            result = chr((columnNumber-1)%26 + ord('A')) + result
            columnNumber = (columnNumber-1) // 26
        return result
