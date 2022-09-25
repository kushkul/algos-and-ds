class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_map = {}
        for ind,val in enumerate(nums):
            if val not in my_map:
                my_map[val]=[ind]
            else:
                my_map[val].append(ind)
        
        for key,val in my_map.items():
            if len(val)>1:
                diffs=[val[i+1]-val[i] for i in range(len(val)-1)]
                if any(x<=k for x in diffs):
                    return True
        return False
