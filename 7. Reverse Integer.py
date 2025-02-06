class Solution:
    def reverse(self, x: int) -> int:
        
        if x<0:
            signed = True
            x*=-1
        else:
            signed = False
        temp,x=pow(2,31),int(str(x)[::-1])
        if signed and x<temp or not signed and x<=temp:
            return -x if signed else x
        return 0


        
