class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        import heapq


class Solution:
    def minInterval(
        self,
        intervals: list[list[int]],
        queries: list[int]
    ) -> list[int]:

        # I sort by start so intervals become
        # eligible in the same order as queries
        intervals.sort()

        # I keep each query's original index
        # so I can restore the requested order
        sorted_queries = sorted(
            (query, i)
            for i, query in enumerate(queries)
        )

        # I default every query to no valid interval
        res = [-1] * len(queries)

        # The heap prioritizes the shortest
        # currently eligible interval
        heap = []
        i = 0

        for query, query_i in sorted_queries:

            # I add every interval that has
            # started by the current query
            while (
                i < len(intervals)
                and intervals[i][0] <= query
            ):
                left, right = intervals[i]

                # I store the length first so
                # the shortest interval stays on top
                length = right - left + 1

                heapq.heappush(
                    heap,
                    (length, right)
                )

                i += 1

            # I remove intervals that end
            # before the current query
            while (
                heap
                and heap[0][1] < query
            ):
                heapq.heappop(heap)

            # After cleanup, the heap top is
            # the shortest interval containing query
            if heap:
                res[query_i] = heap[0][0]

        return res