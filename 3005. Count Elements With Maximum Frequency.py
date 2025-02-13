class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = dict()
        maxFrequency = 0
        for n in nums:
            count[n] = count.get(n,0) + 1
            maxFrequency = max(maxFrequency,count[n])
        result = 0
        for cnt in count.values():
            if cnt == maxFrequency:
                result+=cnt
        return result
            
        
