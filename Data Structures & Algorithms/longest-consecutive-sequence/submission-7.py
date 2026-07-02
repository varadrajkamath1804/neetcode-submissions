class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            if not nums:
                return 0

            sorted_nums = sorted(set(nums))
            print(sorted_nums)
            count=1
            max_count=1
            old_val=sorted_nums[0]
            for num in sorted_nums:
                if num-old_val==1:
                    count=count+1
                else:
                    count=1
                max_count = max(max_count, count)
                old_val=num
            return max_count
            