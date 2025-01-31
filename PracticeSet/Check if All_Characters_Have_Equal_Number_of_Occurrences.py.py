class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        m = set(s)
        print(m)
        h={}
        for char in s:
            if char in h:
                h[char]+=1
            else:
                h[char]=1
        return len(set(h.values())) == 1
            