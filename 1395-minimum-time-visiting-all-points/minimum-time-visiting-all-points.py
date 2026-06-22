class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time=0
        for i in range(0,len(points)-1):
            x,y=points[i]
            a,b=points[i+1]

            time+=max(abs(a-x),abs(b-y))

        return time