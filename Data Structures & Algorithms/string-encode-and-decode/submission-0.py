class Solution:

    def encode(self, strs: List[str]) -> str:
        y=[]
        for i in range(len(strs)):
            x=len(strs[i])
            y.append(f"{x}#{strs[i]}")
        s="".join(y)
        return s
    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i < len(s):
            j=i
            while s[j]!="#":
                j=j+1
            length=int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res
