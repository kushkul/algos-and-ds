class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n==1:
            return True
        for num in itertools.permutations(str(n)):
            if num[0]=='0':
                continue
            if bin(int("".join(w for w in num))).count('1')==1:
                return True
        return False
