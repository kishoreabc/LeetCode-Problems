class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = format(start,'b')
        goal = format(goal,'b')
        i = len(start)-1
        j = len(goal)-1
        result = 0
        print(start,goal)
        while i>=0 or j>=0:
            if i>=0 and j>=0 and start[i] != goal[j]:
                result+=1
                i-=1
                j-=1
            elif i>=0 and j<0 and start[i]=='1':
                result+=1
                i-=1
            elif j>=0 and i<0 and goal[j]=='1':
                result+=1
                j-=1
            else:
                i-=1
                j-=1
        return result
