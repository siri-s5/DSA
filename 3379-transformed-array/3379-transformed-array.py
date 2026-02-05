class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] == 0:
                result.append(0)
            else:
                new_index = (i + nums[i]) % n
                result.append(nums[new_index])
        return result