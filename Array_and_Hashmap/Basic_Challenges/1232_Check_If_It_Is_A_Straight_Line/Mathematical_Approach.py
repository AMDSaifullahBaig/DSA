class Solution(object):
    def checkStraightLine(self, coordinates):
        y,x=coordinates[0]
        y1,x1=coordinates[1]
        xslope,yslope=x1-x,y1-y
        for Y,X in coordinates:
            if (Y-y)*xslope!=(X-x)*yslope:
                return False
        return True