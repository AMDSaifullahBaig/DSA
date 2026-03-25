class Solution:
	def isSameTree(self,p, q):
		queue=deque([(p,q)])
		while queue:
			pn,qn=queue.popleft()
			if not pn and qn:continue
			if not pn or qn or pn.val!=qn.val:return False
			queue.append((pn.left,qn.left))
			queue.append((pn.right,qn.right))
		return True