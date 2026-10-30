from typing import List
from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}
        indegree = {char: 0 for char in graph}

        # Build graph using adjacent words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # Invalid case: longer word comes before its prefix
            # Example: ["abc", "ab"]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            # Find first different character
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    parent = w1[j]
                    child = w2[j]

                    if child not in graph[parent]:
                        graph[parent].add(child)
                        indegree[child] += 1
                    
                    break

        # Start with characters having no dependency
        queue = deque()
        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)

        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for nei in graph[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        # If cycle exists, not all characters will be processed
        if len(result) != len(indegree):
            return ""

        return "".join(result)