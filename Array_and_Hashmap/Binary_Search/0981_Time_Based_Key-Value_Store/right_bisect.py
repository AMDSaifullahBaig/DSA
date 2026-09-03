class TimeMap:
    def __init__(self):
        self.hash={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key]=[]
        self.hash[key].append((value,timestamp))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash:return ""
        l=0
        r=len(self.hash[key])-1
        answer=""
        while l<=r:
            middle=(l+r)//2
            if self.hash[key][middle][1]<=timestamp:
                answer=self.hash[key][middle][0]
                l=middle+1
            else:
                r=middle-1
        return answer