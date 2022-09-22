class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        if n==0:
            return False
        x = math.log(n) / math.log(3)
        if abs(x-int(x))<0.0001 or abs(x-(int(x)+1))<0.0001:
            return True
        return False
