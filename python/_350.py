class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_map1 = {}
        my_map2 = {}
        inter_map = {}
        inter_set = set(nums1).intersection(set(nums2))
        for i in nums1:
            if i in my_map1.keys():
                my_map1[i]+=1
            else:
                my_map1[i]=1
        for i in nums2:
            if i in my_map2.keys():
                my_map2[i]+=1
            else:
                my_map2[i]=1
        for item in inter_set:
            inter_map[item]=min(my_map1[item],my_map2[item])
        
        final = [[i]*j for i,j in inter_map.items()]
        return [j for i in final for j in i]
