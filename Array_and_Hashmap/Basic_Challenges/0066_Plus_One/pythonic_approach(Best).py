class Solution(object):
    def plusOne(self, digits):
        string="".join(map(str,digits))
        num=int(string)+1
        return [int(i) for i in str(num)]