class Solution(object):
    def longestPalindrome(self, s):
        if len(s)>1:
            if s==s[::-1]:
                return s
            maxstr=""
            for i in range(len(s)):
                for j in range(len(s)-1,i,-1):
                    if(i<=j):
                        if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1])>len(maxstr):
                            maxstr=s[i:j+1]
            if maxstr=="":
                return s[0]
            return maxstr
        return s


        
