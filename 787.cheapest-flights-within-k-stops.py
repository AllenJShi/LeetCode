#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        distance = [inf]*n
        distance[src] = 0
        adjacent = [[] for _ in range(n)]
        for flight in flights:
            adjacent[flight[0]].append((flight[1],flight[2]))
        
        queue = deque([(0,(src,0))])
        print(adjacent)
        while queue:
            print(queue)
            dist_, (src_, step_) = queue.popleft()
            for dst_, dist in adjacent[src_]:
                if distance[dst_] > dist_+dist and step_<=k:
                    distance[dst_] = dist_+dist
                    queue.append((distance[dst_],(dst_,step_+1)))
                                    
        return -1 if distance[dst]==inf else distance[dst]
        """
                
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, k+1)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w+dw, y, k-1))
        return -1
# @lc code=end

