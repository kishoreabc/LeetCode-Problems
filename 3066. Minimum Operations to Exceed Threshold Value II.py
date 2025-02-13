class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        min1 = min2 = 0
        result = 0
        while min1<k:
            min1 = heapq.heappop(nums)
            if min1 >=k:
                return result
            min2 = heapq.heappop(nums)
            heapq.heappush(nums,min1*2 +min2)
            result+=1

        
