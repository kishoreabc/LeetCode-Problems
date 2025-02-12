class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n =len(nums)
        result = []
        count = Counter(nums)
        for key,cnt in count.items():
            if cnt>1:
                result.append(key)
                break
        nums = set(nums)
        print(result)
        for i in range(1,n+1):
            if i not in nums:
                return result + [i]

            

