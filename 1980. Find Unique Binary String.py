class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        for n in nums:
            result.append(int(n,2))
        result.sort()
        for i in range(2**len(nums[0])+1):
            if i not in result:
                return format(i,'b').zfill(len(nums[0]))
        

