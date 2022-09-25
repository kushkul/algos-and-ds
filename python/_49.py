class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map={}
        for x in strs:
            sorted_str = ''.join(sorted(x, key=str.lower))
            if sorted_str in my_map.keys():
                my_map[sorted_str].append(x)
            else:
                my_map[sorted_str]=[x]
        return [item for item in my_map.values()]
