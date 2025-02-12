class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        count = 0
        for char in s:
            if char.isalpha():
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    count+=1
            if count and stack:
                count-=1
                stack.pop()
        return "".join(stack)

        
