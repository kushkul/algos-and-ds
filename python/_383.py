class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mymap={}
        for item in ransomNote:
            if item in mymap.keys():
                mymap[item]+=1
            else:
                mymap[item]=1
        
        for item in magazine:
            if item in mymap.keys() and mymap[item]>0:
                mymap[item]-=1
        
        val_set=set(mymap.values())
        if len(val_set)==1 and list(val_set)[0]==0:
            return True
        return False
