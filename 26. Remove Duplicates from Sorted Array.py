class Solution(object):
    def removeDuplicates(self, nums):
        not_Unique,i=0,0
        while i<len(nums)-not_Unique:
            if nums[i] in nums[:i]:
                nums.remove(nums[i])
                nums.append("_")
                not_Unique+=1
            else:
                i+=1
        return i
