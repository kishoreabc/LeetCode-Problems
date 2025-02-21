class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=list()
        intervals.sort()
        flag=True
        while flag and len(intervals)>1:
            for i in range(len(intervals)-1):
                if intervals[i][1] >=intervals[i+1][0]:
                    flag=True
                    intervals[i][1]=max(intervals[i+1][1],intervals[i][1])
                    intervals.pop(i+1)
                    break
                else:
                    flag=False
        return intervals
