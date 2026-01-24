class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxi=0
        a=0
        b=len(nums)-1
        while a<b:
            c=nums[a]+nums[b]
            maxi=max(maxi,c)
            a+=1
            b-=1
        return maxi