class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def intToBin(num,base):
            result = []
            while num:
                result.insert(0,str(num % base))
                num//=base
            return "".join(result)
        for i in range(2,n-1):
            binary = intToBin(n,i)
            if binary != binary[::-1]:
                return False
        return True
