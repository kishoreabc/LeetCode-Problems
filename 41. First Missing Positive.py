class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxi = -1
        for i in range(1,100001):
            maxi = max(maxi,i)
            if i not in nums:
                return i
        return maxi+1
            
