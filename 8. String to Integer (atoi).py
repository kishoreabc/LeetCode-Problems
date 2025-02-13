class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        encounter = 0
        for n in s:
            if n in ' ' and not encounter:
                continue
            elif n in '-+' and not encounter:
                sign = 0 if n == '-' else 1
                encounter = 1
            elif ord(n) >=48 and ord(n) <= 57:
                result*=10
                result+=int(n)
                encounter = 1
                print(result)
            else:
                break
        result = result if sign else result*-1
        upper = 2**31-1
        lower = -2**31

        if result >= upper:
            return upper
        if result <= lower:
            return lower
        return result


        
