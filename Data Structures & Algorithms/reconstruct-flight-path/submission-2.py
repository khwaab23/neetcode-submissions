# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         from collections import defaultdict
# import heapq
# from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Store destinations in min heaps for lexical order.
        for source, destination in tickets:
            heapq.heappush(graph[source], destination)

        route = []

        def dfs(airport: str) -> None:
            # Consume every ticket leaving this airport.
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)

            # Add only after all outgoing tickets are used.
            route.append(airport)

        dfs("JFK")

        # Hierholzer builds the itinerary backward.
        return route[::-1]