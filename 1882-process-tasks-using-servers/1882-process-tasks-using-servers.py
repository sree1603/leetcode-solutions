class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        available = []
        busy = []

        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        result = []

        for time, duration in enumerate(tasks):

            while busy and busy[0][0] <= time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            if not available:
                free_time, weight, index = heapq.heappop(busy)

                result.append(index)

                heapq.heappush(
                    busy,
                    (free_time + duration, weight, index)
                )

            else:
                weight, index = heapq.heappop(available)

                result.append(index)

                heapq.heappush(
                    busy,
                    (time + duration, weight, index)
                )

        return result
