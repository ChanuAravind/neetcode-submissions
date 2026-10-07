class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        groups = {}
        for i in range(len(nums)):
            if nums[i] not in groups:
                groups[nums[i]] = 0
            groups[nums[i]] += 1
        sorted_groups = sorted(list(groups.items()),key = lambda x:x[1],reverse=True)
        
        return [x[0] for x in sorted_groups[:k]]