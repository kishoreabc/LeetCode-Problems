class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product = nums[i]*nums[j]
                count[product] = count.get(product,0) + 1
        result = 0
        for cnt in count.values():
            pair = cnt*(cnt-1) //2
            result += pair*8
        return result
# https://www.youtube.com/watch?v=SSwvMoOhiq0

        
        
