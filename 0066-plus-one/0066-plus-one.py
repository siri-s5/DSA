class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = int("".join(map(str, digits)))
        r+=1
        l = [int(digit) for digit in str(r)]
        return l