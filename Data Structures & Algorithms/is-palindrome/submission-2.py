class Solution:
    def isPalindrome(self, s: str) -> bool:
        start=0
        end=len(s)-1
        lower=s.lower()
        while start<end:
            
            if lower[start].isalnum()==False:
                start+=1
                continue
            if lower[end].isalnum()==False:
                end-=1
                continue
            
            if lower[start] != lower[end]:
                return False
            start=start+1
            end=end-1
        return True
            