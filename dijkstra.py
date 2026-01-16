import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight):
        """Add a weighted edge from u to v"""
        self.graph[u].append((v, weight))
    
    def dijkstra(self, start, end):
        """
        Find shortest path from start to end using Dijkstra's algorithm
        Returns: (shortest_distance, path)
        """
        # Priority queue: (distance, node, path)
        pq = [(0, start, [start])]
        # Track visited nodes
        visited = set()
        # Store minimum distances
        distances = {start: 0}
        
        while pq:
            curr_dist, curr_node, path = heapq.heappop(pq)
            
            # Skip if already visited
            if curr_node in visited:
                continue
            
            visited.add(curr_node)
            
            # Found the destination
            if curr_node == end:
                return curr_dist, path
            
            # Explore neighbors
            for neighbor, weight in self.graph[curr_node]:
                if neighbor not in visited:
                    new_dist = curr_dist + weight
                    
                    # Update if we found a shorter path
                    if neighbor not in distances or new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor, path + [neighbor]))
        
        # No path found
        return float('inf'), []
    
    def print_graph(self):
        """Display the graph structure"""
        print("\nGraph Structure:")
        for node in sorted(self.graph.keys()):
            print(f"{node}: {self.graph[node]}")


# Example usage
if __name__ == "__main__":
    # Create graph
    g = Graph()
    
    # Add edges (node1, node2, weight)
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)
    g.add_edge('D', 'F', 6)
    g.add_edge('E', 'F', 3)
    
    # Display graph
    g.print_graph()
    
    # Find shortest path
    start_node = 'A'
    end_node = 'F'
    
    distance, path = g.dijkstra(start_node, end_node)
    
    print(f"\nShortest path from {start_node} to {end_node}:")
    print(f"Distance: {distance}")
    print(f"Path: {' -> '.join(path)}")
    
    # Test another path
    print("\n" + "="*50)
    start_node = 'A'
    end_node = 'E'
    distance, path = g.dijkstra(start_node, end_node)
    print(f"\nShortest path from {start_node} to {end_node}:")
    print(f"Distance: {distance}")
    print(f"Path: {' -> '.join(path)}")