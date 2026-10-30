from collections import defaultdict


class Solution:
    def findItinerary(
        self,
        tickets
    ):

        # I group all destinations for each airport
        graph = defaultdict(list)

        # I sort once so smaller airports are chosen first
        tickets.sort(reverse=True)

        # I build the adjacency list
        for src, dst in tickets:
            graph[src].append(dst)

        # I store the itinerary in reverse order
        itinerary = []

        def dfs(airport):

            # I keep using tickets until none remain
            while graph[airport]:

                # The smallest destination is now at the end
                next_airport = graph[airport].pop()

                dfs(next_airport)

            # I add the airport only after using every ticket
            itinerary.append(airport)

        # The journey always starts from JFK
        dfs("JFK")

        # I reverse because airports were added postorder
        return itinerary[::-1]