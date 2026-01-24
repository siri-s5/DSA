class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=0
        prev1=0
        for i in nums:
            curr=max(prev,prev1+i)
            prev1=prev
            prev=curr
        return prev