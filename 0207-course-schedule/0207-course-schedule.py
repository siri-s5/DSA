#from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for course,destination in prerequisites:
            graph[destination].append(course)
            indegree[course]+=1
        q=deque([])
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        finish=0
        while q:
            node=q.popleft()
            finish+=1
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return finish==numCourses

        
        # Step 1: graph
 #       graph = {i: [] for i in range(numCourses)}
        
        # Step 2: indegree
  #      indegree = {i: 0 for i in range(numCourses)}

        # Step 3: fill graph and indegree
   #     for a, b in prerequisites:
    #        graph[b].append(a)
     #       indegree[a] += 1

        # Step 4: queue
      #  queue = deque()
       # for i in range(numCourses):
        #    if indegree[i] == 0:
         #      queue.append(i)

        # Step 5: BFS
       # count = 0

        #while queue:
         #   node = queue.popleft()
          #  count += 1

           # for nei in graph[node]:
            #    indegree[nei] -= 1

             #   if indegree[nei] == 0:
              #      queue.append(nei)

        # Step 6: result
       # return count == numCourses

#create empty graph-->fill the graph-->fill indegree-->check 0-indegree-->append to queue-->while queue-->node=queue.popleft() count+=1-->check indegree and then count 