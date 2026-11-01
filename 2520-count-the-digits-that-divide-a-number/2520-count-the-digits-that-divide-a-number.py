class Solution:
    def countDigits(self, num: int) -> int:
        temp=num
        count=0
        while num>0:
            a=num%10
            if temp%a==0:
                count+=1
            num=num//10
        return count