class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums)<4:
            return False
        i=0
        n=len(nums)
        while i+1 < n and nums[i] < nums[i+1]:
            i += 1
        if i == 0:
            return False  
        j=i
        while i+1 < n and nums[i] > nums[i+1]:
            i += 1
        if i == j:
            return False 
        k = i 
        while i+1 < n and nums[i] < nums[i+1]:
            i += 1
        if i==k:
            return False
        return i==n-1


