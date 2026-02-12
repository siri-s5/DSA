class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            freq = {}
            distinct = 0
            max_freq = 0
            for j in range(i, n):
                ch = s[j]
                if ch not in freq:
                    freq[ch] = 1
                    distinct += 1
                else:
                    freq[ch] += 1
                max_freq = max(max_freq, freq[ch])
                length = j - i + 1
                if max_freq * distinct == length:
                    max_len = max(max_len, length)
        return max_len