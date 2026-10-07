class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_map = {}
        
        for i in range(len(nums)):
            if target-nums[i] in index_map:
                return [index_map[target-nums[i]],i]
            else:
                index_map[nums[i]] = i