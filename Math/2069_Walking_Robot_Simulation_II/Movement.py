class Robot:
    def __init__(self, width: int, height: int):
    	self.width=width-1
    	self.height=height-1
    	self.x=0
    	self.y=0
    	self.dir=0
    	self.arr=["East","North","West","South"]
    	self.moves=[(1,0),(0,1),(-1,0),(0,-1)]
    	self.perimeter=2*(self.width+self.height)
    def step(self, num: int) -> None:
     		num%=self.perimeter
     		if num==0 and self.x==0 and self.y==0:
     			self.dir=3
     		for i in range(num):
     			dx,dy=self.moves[self.dir]
     			x,y=self.x+dx, self.y+dy
     			while not (0<=x<=self.width and 0<=y<=self.height):
     				self.dir=(self.dir+1)%4
     				dx,dy=self.moves[self.dir]
     				x,y=self.x+dx,self.y+dy
     			self.x,self.y=x,y
        def getPos(self) -> List[int]:
    	return [self.x,self.y]
    def getDir(self) -> str:
    	return self.arr[self.dir]