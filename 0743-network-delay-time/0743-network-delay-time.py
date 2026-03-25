class Solution:
    def networkDelayTime(self, times, n, k):
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0
        pq = [(0, k)]
        while pq:
            time, node = heapq.heappop(pq)
            if time > dist[node]:
                continue
            for nei, wt in adj[node]:
                if time+wt <dist[nei]:
                    dist[nei]=time+wt
                    heapq.heappush(pq.(dist[nei],max_time=max(dist[1:])))
                    if max_time!=float('inf'):
                        return max_time
                    else:
                        return -1