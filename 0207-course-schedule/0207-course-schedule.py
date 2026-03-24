from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        # Step 1: graph
        graph = {i: [] for i in range(numCourses)}
        
        # Step 2: indegree
        indegree = {i: 0 for i in range(numCourses)}

        # Step 3: fill graph and indegree
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # Step 4: queue
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Step 5: BFS
        count = 0

        while queue:
            node = queue.popleft()
            count += 1

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        # Step 6: result
        return count == numCourses