class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref)<2:
            return pref
        last = 0
        result = []
        for n in pref:
            result.append(n^last)
            last = n
        return result
