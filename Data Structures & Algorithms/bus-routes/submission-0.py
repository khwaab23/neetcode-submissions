class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        n=len(routes)
        stops=defaultdict(list)
        for bus in range(n):
            for stop in routes[bus]:
                stops[stop].append(bus)

        bus_seen=set()
        stop_seen=set([source])
        res=0
        q=deque([source])
        while q:
            for _ in range(len(q)):
                stop=q.popleft()
                if stop==target:
                    return res
                for bus in stops[stop]:
                    if bus in bus_seen:
                        continue
                    bus_seen.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop in stop_seen:
                            continue
                        q.append(next_stop)
                        stop_seen.add(next_stop)
            res+=1
        return -1