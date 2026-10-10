class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        longest_length =0
        
        for i in nums_set:
            curr_longest =1
            if i-1 not in nums_set:
                check_num = i+1
                while check_num in nums_set:
                    curr_longest+=1
                    check_num+=1

                longest_length = max(longest_length,curr_longest)

        return longest_length