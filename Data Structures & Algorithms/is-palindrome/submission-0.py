class Solution:
    def isPalindrome(self, s: str) -> bool:
        news=""
        for i in range(len(s)):
            if s[i].isalnum():
                news=news+s[i]
        news=news.lower()
        start=0
        end=len(news)-1
        while start<end:
            if news[start]==news[end]:
                start+=1
                end-=1
            else:
                return False 
        return True