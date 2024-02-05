import heapq


class HeapNode:
    def __init__(self, distance, node):
        self.distance = distance
        self.node = node

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __str__(self):
        return str(self.distance)

    def __repr__(self):
        return f"HeapNode(distance={self.distance}, node={self.node})"


if __name__ == "__main__":
    min_heap = []
    heapq.heappush(min_heap, HeapNode(1, 2))
    heapq.heappush(min_heap, HeapNode(2, "B"))
    heapq.heappush(min_heap, HeapNode(5, "B"))
    heapq.heappush(min_heap, HeapNode(-1, "A"))
    heapq.heappush(min_heap, HeapNode(10, "B"))
    heapq.heappush(min_heap, HeapNode(3, "A"))
    print(min_heap)

    print(heapq.heappop(min_heap))  # -> -1
    print(heapq.heappop(min_heap))  # -> 1

    print(min_heap)
