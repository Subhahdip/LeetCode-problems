class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == [[]]:
            return []
        intervals.sort()
        newlist =[] 
        interval = intervals[0]
        for i in intervals:

            if i[0] <= interval[1]:
                interval[1] = max(interval[1],i[1])
            else:
                newlist.append(interval)
                interval = i
                
        newlist.append(interval)
        return newlist
                