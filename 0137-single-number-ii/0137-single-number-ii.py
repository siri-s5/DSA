class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for num in freq:
            if freq[num]==1:
                return num