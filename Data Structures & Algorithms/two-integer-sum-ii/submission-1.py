class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s={}
        for i in range (len(numbers)):
            need=target-numbers[i]
            if need in s:
                return [s[need],i+1]
            else:
                s[numbers[i]]=i+1