class Solution:
 def numberOfSpecialChars(self,word:str)->int:
  lower,upper=[-1]*26,[-1]*26
  for i,ch in enumerate(word):
   if'a'<=ch<='z':lower[ord(ch)-ord('a')]=i
   else:
    idx=ord(ch)-ord('A')
    if upper[idx]==-1:upper[idx]=i
  ans=0
  for i in range(26):
   if lower[i]!=-1 and upper[i]!=-1 and lower[i]<upper[i]:ans+=1
  return ans
