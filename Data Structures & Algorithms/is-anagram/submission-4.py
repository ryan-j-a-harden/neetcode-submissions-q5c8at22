class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s, key=str.lower))
        t = "".join(sorted(t, key=str.lower))
        
        reversed_string = "".join(reversed(t))

        return s == t and len(s) == len(t)