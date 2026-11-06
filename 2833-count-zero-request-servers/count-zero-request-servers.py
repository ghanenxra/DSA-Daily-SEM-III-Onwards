from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by timestamp
        logs.sort(key=lambda item: item[1])
        
        # Sort queries along with their original indices
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        server_count = {}
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        for original_idx, q in sorted_queries:
            window_start = q - x
            window_end = q
            
            # Add logs that fall within the right boundary (<= window_end)
            while right < num_logs and logs[right][1] <= window_end:
                server_id = logs[right][0]
                server_count[server_id] = server_count.get(server_id, 0) + 1
                right += 1
                
            # Remove logs that fall outside the left boundary (< window_start)
            while left < num_logs and logs[left][1] < window_start:
                server_id = logs[left][0]
                server_count[server_id] -= 1
                if server_count[server_id] == 0:
                    del server_count[server_id]
                left += 1
                
            # Servers with zero requests = total servers (n) - servers with at least 1 request
            ans[original_idx] = n - len(server_count)
            
        return ans