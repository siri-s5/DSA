import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        
        for u, v, w in flights:
            adj[u].append((v, w))
        
        pq = [(0, src, 0)]  # (cost, node, stops)
        
        # Track best stops to reach a node
        stops = [float('inf')] * n
        
        while pq:
            cost, node, step = heapq.heappop(pq)
            
            if node == dst:
                return cost
            
            if step > k or step > stops[node]:
                continue
            
            stops[node] = step
            
            for nei, price in adj[node]:
                heapq.heappush(pq, (cost + price, nei, step + 1))
        
        return -1