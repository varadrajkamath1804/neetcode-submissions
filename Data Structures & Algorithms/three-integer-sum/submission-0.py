class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        number_sorted=sorted(nums)
        for i in range(n-2):
            if i>0 and number_sorted[i]==number_sorted[i-1]:
                continue

            j= i+1
            k= n-1
            while j<k:
                total= number_sorted[i]+number_sorted[j]+number_sorted[k]
                if total > 0:
                    k-=1
                elif total<0:
                    j+=1
                else:
                    result.append([number_sorted[i],number_sorted[j],number_sorted[k]])
                    j+=1
                    k-=1

                    while j<k and number_sorted[j]==number_sorted[j-1]:
                        j+=1
                
                    while j<k and number_sorted[k]==number_sorted[k+1]:
                        k-=1
                        
                    
                
        return result
                    
                
