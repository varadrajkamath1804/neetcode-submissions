class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= "".join(sorted(s))
        t= "".join(sorted(t))
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        for j in t:
            freq[j]=freq.get(j,0)-1
        if all(val==0 for val in freq.values()):
            return True
        return False

