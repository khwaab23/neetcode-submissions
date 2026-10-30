import heapq


class Node:
    def __init__(self, val=0, node_id=0):
        self.val = val
        self.node_id = node_id
        self.prev = None
        self.next = None
        self.removed = False


class MaxStack:
    def __init__(self):
        # Dummy nodes let me add or remove nodes
        # without separate boundary logic
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.heap = []
        self.next_id = 0

    def _add_node(self, node):
        # I insert before tail because that position
        # always represents the top of the stack
        previous = self.tail.prev

        previous.next = node
        node.prev = previous

        node.next = self.tail
        self.tail.prev = node

    def _remove_node(self, node):
        # Since I already know the node, the linked
        # list lets me remove it in constant time
        node.prev.next = node.next
        node.next.prev = node.prev
        node.removed = True

    def _clean_heap(self):
        # A normal pop may leave an old node in the
        # heap, so I discard it only when it reaches top
        while (
            self.heap
            and self.heap[0][2].removed
        ):
            heapq.heappop(self.heap)

    def push(self, x):
        node = Node(x, self.next_id)
        self.next_id += 1

        self._add_node(node)

        # The larger ID wins when values are equal,
        # which gives me the topmost maximum
        heapq.heappush(
            self.heap,
            (
                -x,
                -node.node_id,
                node,
            ),
        )

    def pop(self):
        node = self.tail.prev
        self._remove_node(node)

        return node.val

    def top(self):
        # The node before tail is always the current top
        return self.tail.prev.val

    def peekMax(self):
        self._clean_heap()

        return -self.heap[0][0]

    def popMax(self):
        self._clean_heap()

        _, _, node = heapq.heappop(
            self.heap
        )

        self._remove_node(node)

        return node.val