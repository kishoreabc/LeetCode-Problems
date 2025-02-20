class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(score)-1):
            Max = i
            for j in range(i+1,len(score)):
                Max = j if score[j][k]>score[Max][k] else Max
            score[i],score[Max] = score[Max],score[i]
        return score
            

