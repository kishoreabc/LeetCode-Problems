class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digits = dict()
        result = -1
        for i in range(len(nums)):
            temp = 0
            for n in str(nums[i]):
                temp+=int(n)
            digits[temp] = digits.get(temp,[])+[nums[i]]
            if len(digits[temp])>2:
                digits[temp].sort()
                digits[temp].pop(0)
            if len(digits[temp])==2:
                result = max(result,sum(digits[temp]))
        print(digits)
        return result


        
