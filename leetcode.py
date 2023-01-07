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


#leetcode 392 is subsequence
class Solution392():
    def issubsequence(self, s:str,l:str)->bool:
        i,j=0,0
        while i<len(s) and j<len(l):
            if s[i]==l[j]:
                i+=1
            j+=1
        return i==len(s)


#leetcode 58 length of last word
class Solution58:
    def lenghoflastword(self,s:str):
        i,length=len(s)-1,0
        while s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            length+=1
            i-=1
        return length
