class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for list_item in strs:
            sorted_version= "".join(sorted(list_item))
           
            if sorted_version not in freq:
                freq[sorted_version]=[]

            freq[sorted_version].append(list_item)
        return list(freq.values())

            
            

        

            
                