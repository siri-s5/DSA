class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #freq={}
        #for i in nums:
        #    freq[i]=freq.get(i,0)+1
        #for num in freq:
        #    if freq[num]==1:
        #        return num
        nums.sort()
        i=0
        n=len(nums)
        while i<n-1 and nums[i]==nums[i+1]:
            i+=3
        return nums[i]
