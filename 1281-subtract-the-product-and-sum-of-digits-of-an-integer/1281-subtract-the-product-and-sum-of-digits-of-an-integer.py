class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        b=0
        c=1
        while n>0:
            a=n%10
            b=b+a
            c=c*a
            n=n//10
        d=c-b
        return d