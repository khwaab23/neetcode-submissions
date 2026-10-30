class MaxStack:

    def __init__(self):
        # One stack keeps the values, while the other
        # keeps the maximum at every stack position
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        # I carry the previous maximum forward so the
        # current maximum is always available at the top
        if self.max_stack:
            current_max = max(
                x,
                self.max_stack[-1]
            )
        else:
            current_max = x

        self.max_stack.append(
            current_max
        )

    def pop(self) -> int:
        # Both stacks represent the same positions,
        # so I remove from both when the top is removed
        self.max_stack.pop()

        return self.stack.pop()

    def top(self) -> int:
        # The final element is the current stack top
        return self.stack[-1]

    def peekMax(self) -> int:
        # The final maximum entry represents the
        # maximum across the entire current stack
        return self.max_stack[-1]

    def popMax(self) -> int:
        max_value = self.peekMax()
        buffer = []

        # Searching from the top ensures I remove the
        # topmost occurrence when the maximum repeats
        while self.top() != max_value:
            buffer.append(
                self.pop()
            )

        self.pop()

        # I restore the removed values in their
        # original order and rebuild their maximums
        while buffer:
            self.push(
                buffer.pop()
            )

        return max_value