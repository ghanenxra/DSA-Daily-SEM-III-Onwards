import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))
        heapq.heapify(free)
        busy = []
        handled = [0] * k
        
        for i, (t, d) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:
                _, server_id = heapq.heappop(busy)
                heapq.heappush(free, i + (server_id - i) % k)
            if free:
                virtual_turn = heapq.heappop(free)
                server_id = virtual_turn % k
                heapq.heappush(busy, (t + d, server_id))
                handled[server_id] += 1
        max_handled = max(handled)
        return [i for i, count in enumerate(handled) if count == max_handled]