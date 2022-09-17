class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import defaultdict
        stone_map = defaultdict(int)
        for i in stones:
            stone_map[i]+=1
        
        total=0
        for i in jewels:
            if i in stone_map.keys():
                total += stone_map[i]
        return total
