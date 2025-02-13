class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        for n in nums:
            if n>=k:
                break
            result+=1
        return result  
