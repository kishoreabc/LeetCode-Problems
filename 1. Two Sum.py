class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = []
        for i in range(len(nums)):
            Sum = target-nums[i]
            if Sum in temp:
                return [temp.index(Sum),i]
            temp.append(nums[i])
            
