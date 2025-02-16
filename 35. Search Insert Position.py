class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        try:
            
            while nums[i]<target:
                i+=1
        except(IndexError):
            return i
        return i
