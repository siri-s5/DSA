class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        nums.sort()
        mini = float('inf')
        for i in range(len(nums) - k + 1):
            mini = min(mini, nums[i + k - 1] - nums[i])
        return mini