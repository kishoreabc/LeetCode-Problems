class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        Sum = 0
        for n in num:
            Sum*=10
            Sum+=n
        Sum+=k
        result = []
        while Sum:
            result.append(Sum%10)
            Sum//=10
        return result[::-1]
