class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distance = [ target - i for i in position]
        n = len(position)
        cars = [(distance[i],speed[i]) for i in range(n) ]
        cars.sort()
        # time  = [d/s for d,s in zip(distance, speed)]
        time = []
        fleet = 0
        for d,s in cars:
            if not time :
                time.append(d/s)
                fleet+=1
            elif d/s > time[-1]:
                time.append(d/s)
                fleet+=1
            
        return fleet


