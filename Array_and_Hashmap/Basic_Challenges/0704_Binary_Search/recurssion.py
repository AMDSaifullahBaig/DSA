class Solution(object):
	    def search(self, nums, target):
	           def binarysearch(start,stop,val):
	           	 if start>stop:
	           	 	return -1
	           	 middle=(start+stop)//2
	           	 if nums[middle]==val:
	           	 	return middle
	           	 elif nums[middle]>val:
	           	 	return binarysearch(start,middle-1,val)
	           	 else:
	           	 	return binarysearch(middle+1,stop,val)
	           return binarysearch(0,len(nums)-1,target)