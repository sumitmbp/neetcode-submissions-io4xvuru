class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        val=float("-inf")
        if not nums:
            return 0
        for i in nums:
            s.add(i)
        for num in s:
            if num-1 not in s:
                current=num
                count=1
                while current+1 in s:
                    current+=1
                    count+=1
                val=max(count,val)
        return val
        