class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber>26:
            result = chr((columnNumber-1)%26 + ord('A')) + result
            columnNumber = (columnNumber-1) // 26
        result = (chr((columnNumber-1)+ ord('A')) if columnNumber else "") + result
        return result
