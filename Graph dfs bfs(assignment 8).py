# lab assignment 8
# Perform BFS and DFS on a graph.

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    print(start, end=" ")
    visited.add(start)
    for neighbour in graph[start] - visited:
        dfs(graph, neighbour, visited)

# Main Program
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A', 'E'},
    'D': {'B'},
    'E': {'C'}
}

print("BFS Traversal:")
bfs(graph, 'A')

print("\nDFS Traversal:")
dfs(graph, 'A')
