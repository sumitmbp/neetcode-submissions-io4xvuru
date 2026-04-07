class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1={}
        h1={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in s1:
                s1[s[i]]+=1
            else:
                s1[s[i]]=1
            if t[i] in h1:
                h1[t[i]]+=1
            else:
                h1[t[i]]=1
        return s1==h1

            

        