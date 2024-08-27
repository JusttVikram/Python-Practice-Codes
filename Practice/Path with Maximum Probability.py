# Leetcode 1514.

from collections import defaultdict, deque
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        max_prob = [0] * n
        max_prob[start_node] = 1
        q = deque([start_node])
        
        while q:
            node = q.popleft()
            for neighbor, prob in graph[node]:
                if max_prob[neighbor] < max_prob[node] * prob:
                    max_prob[neighbor] = max_prob[node] * prob
                    q.append(neighbor)
        
        return max_prob[end_node]