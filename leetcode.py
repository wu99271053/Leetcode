from typing import List


#leetcode 217 contain duplicate
class Solution217:
    def containsDuplicatee(Self,nums:List[int]) ->bool:
        hashset=set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False 



# leetcode 242 valid anagram
class Solution242:
    def isAnagram(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        
        countS,countT={},{}

        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        return countS==countT


#leetcode 1299 replace with the right greatest value
class Solution1299:
    def replace(self,arr:List[int])->List[int]:
        rightMax=-1
        for i in range(len(arr)-1,-1,-1):
            newmax=max(arr[i],rightMax)
            arr[i]=rightMax
            rightMax=newmax
        return arr