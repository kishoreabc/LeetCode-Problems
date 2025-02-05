class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber>26:
            result+=chr((columnNumber-1)%26 +65)
            columnNumber = (columnNumber-1) // 26
        result += chr((columnNumber-1)+65) if columnNumber else ""
        return result[::-1]
