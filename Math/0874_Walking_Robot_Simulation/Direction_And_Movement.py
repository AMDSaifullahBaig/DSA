class Solution:
    def robotSim(self, commands, obstacles):
        obs=set()
        for i in obstacles:
            obs.add((i[0],i[1]))
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        x=0
        y=0
        dir=0
        maximum=0
        for i in commands:
            if i==-1:
                dir=(dir+1)%4
            elif i==-2:
                dir=(dir+3)%4
            else:
                while i>0:
                    x2=x+direction[dir][0]
                    y2=y+direction[dir][1]
                    if (x2,y2) in obs:
                        break
                    x=x2
                    y=y2
                    maximum=max(maximum,x*x+y*y)
                    i-=1
        return maximum