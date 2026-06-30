class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        output=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1

        bucket= [[] for _ in range(len(nums)+1)]

        for num,count in freq.items():
            bucket[count].append(num)
        print(bucket)

        result=[]

        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                print(bucket[i])
                result.append(num)
                

                if len(result)==k:
                    return result
                

                
            