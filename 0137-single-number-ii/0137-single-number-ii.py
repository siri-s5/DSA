class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #freq={}
        #for i in nums:
        #    freq[i]=freq.get(i,0)+1
        #for num in freq:
        #    if freq[num]==1:
        #        return num
        #nums.sort()
        #i=0
        #n=len(nums)
        #while i<n-1 and nums[i]==nums[i+1]:
        #    i+=3
        #return nums[i]
        ans = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1:
                    count += 1
            if count % 3!=0:
                ans |= (1 << i)
        if ans>=2**31:
            ans-=2**32
        return ans