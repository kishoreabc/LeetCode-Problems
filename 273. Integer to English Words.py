class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        ones_map = {
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            10:"Ten",
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen"
        }
        tens_map={
            20:"Twenty",
            30:"Thirty",
            40:"Forty",
            50:"Fifty",
            60:"Sixty",
            70:"Seventy",
            80:"Eighty",
            90:"Ninety"
        }
        result = []
        def helper(n):
            res = []
            hundred = n//100
            n%=100
            if hundred: 
                res.append(ones_map[hundred] + " Hundred")

            if n<20 and n>0:
                res.append(ones_map[n])
            else:
                tens,ones = (n//10)*10,n%10
                if tens:
                    res.append(tens_map[tens])
                if ones:
                    res.append(ones_map[ones])
            return " ".join(res)
        postfix = [""," Thousand"," Million"," Billion"]
        i=0
        while num:
            last3Digit = num%1000 
            s = helper(last3Digit)
            if s:
                result.append(s + postfix[i])
            i+=1
            num//=1000
        print(result) 
        result.reverse()
        return " ".join(result)

