class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum1_l = [a+b for a in nums1 for b in nums2]
        sum2_c = collections.Counter([c+d for c in nums3 for d in nums4])
        
        return sum([sum2_c.get(-1*res1,0) for res1 in sum1_l])
