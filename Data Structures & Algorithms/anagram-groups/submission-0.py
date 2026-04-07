class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in range(len(strs)):
            x=''.join(sorted(strs[i]))
            if x in dict:
                dict[x]+=[strs[i]]
            else:
                dict[x]=[strs[i]]
        y=[]
        for keys in dict:
            y+=[dict[keys]]
        return y

        