import heapq

def min_rooms(intervals):
        intervals.sort()
        
        rooms = 0
        clash = []
        
        for interval in intervals:
            if not clash:
                clash.append(interval[1])
                rooms += 1
            else:
                if interval[0] >= clash[0]:
                    heapq.heappushpop(clash, interval[1])
                    
                else:
                    heapq.heappush(clash, interval[1])
                    rooms += 1
        return rooms
        
inputList = [int(item) for item in input("Enter the time intervals: ").split()]
intervals = [inputList[i: i+2] for i in range(0, len(inputList), 2)]

print(min_rooms(intervals))
