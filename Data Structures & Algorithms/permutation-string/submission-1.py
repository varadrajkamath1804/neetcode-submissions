class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need={}
        for ch in s1:
            need[ch]=need.get(ch,0)+1
        
        window={}
        left=0

        for right in range(len(s2)):
            window[s2[right]]=window.get(s2[right],0)+1

            while right-left+1 > len(s1):
                left_char = s2[left]
                window[left_char]-=1

                if window[left_char]==0:
                    del window[left_char]
                
                left+=1
            
            if window==need:
                return True
        return False



