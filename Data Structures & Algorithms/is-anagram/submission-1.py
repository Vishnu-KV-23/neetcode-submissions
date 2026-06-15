class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cS,cT={},{}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            cS[s[i]]=cS.get(s[i],0)+1
            cT[t[i]]=cT.get(t[i],0)+1
        return cS==cT
    