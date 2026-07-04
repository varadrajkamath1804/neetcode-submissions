class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=[]
        max_count=0
        
        for ch in s:
            
            if ch in longest:
                ind=longest.index(ch)
                longest=longest[ind+1:]
            
            longest.append(ch)
            max_count=max(max_count,len(longest))

        return max_count