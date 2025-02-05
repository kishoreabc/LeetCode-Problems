class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s1 = list(s1)
        s2 = list(s2)
        index1 = index2 = None
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if index1 is not None:
                    s2[index1],s2[i] = s2[i],s2[index1] 
                    break
                else:
                    index1 = i
        return s1 == s2
        
        
