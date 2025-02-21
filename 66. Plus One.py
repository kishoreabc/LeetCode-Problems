class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        while digits:
            num*=10
            num+=digits.pop(0)
        num+=1
        for i in range(len(str(num))):
            digits.insert(0,num%10)
            num//=10
        return digits
