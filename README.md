
# Linked List Reversal

This project demonstrates how to reverse a singly linked list in Python. 

## Problem Statement
Given a singly linked list, reverse the order of its elements.

### Example
- Input: `1 -> 2 -> 3 -> 4 -> 5`
- Output: `5 -> 4 -> 3 -> 2 -> 1`

## Implementation

### Classes

1. **Node**:
   Represents an individual node in the linked list.
   - Contains:
     - `value`: The value stored in the node.
     - `next`: A reference to the next node in the list.

2. **LinkedList**:
   Represents the singly linked list.
   - Contains:
     - `head`: The starting node of the list.
   - Methods:
     - `append(value)`: Adds a node with the given value to the end of the list.
     - `reverse()`: Reverses the list in place.
     - `to_list()`: Converts the linked list to a Python list for easy visualization.

### Algorithm for Reversal

The reversal logic is implemented in the `reverse` method:
1. Use three pointers:
   - `prev`: Tracks the previous node (initialized as `None`).
   - `current`: Tracks the current node (starts as `head`).
   - `next_node`: Temporarily stores the next node.
2. Iteratively:
   - Save the next node (`next_node`).
   - Reverse the link (`current.next = prev`).
   - Move `prev` to the current node.
   - Move `current` to the next node.
3. Update the `head` to the last processed node (`prev`).

This algorithm runs in **O(n)** time and uses **O(1)** additional space.

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of nodes in the list.
  - Each node is visited exactly once.
- **Space Complexity**: O(1).
  - No additional data structures are used apart from a few pointers.

## Example Code

```python
class Node:
    def __init__(self, value):
        # Node stores the value and the reference to the next node
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        # The linked list starts with no head
        self.head = None

    def append(self, value):
        # Add a new node at the end of the list
        new_node = Node(value)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Add the new node

    def reverse(self):
        # Reverse the linked list
        prev = None  # Initialize the previous node
        current = self.head  # Start with the head
        while current:  # Traverse the list
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev to current
            current = next_node  # Move to the next node
        self.head = prev  # Update the head to the last node

    def to_list(self):
        # Convert the linked list to a Python list for easy visualization
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

# Usage
linked_list = LinkedList()
for value in [1, 2, 3, 4, 5]:
    linked_list.append(value)

print("Original List:", linked_list.to_list())
linked_list.reverse()
print("Reversed List:", linked_list.to_list())
```

## How to Run
1. Copy the code above into a Python file (e.g., `linked_list.py`).
2. Run the file using Python:
   ```bash
   python linked_list.py
   ```
3. You will see the original and reversed lists printed.

## Output Example

```
Original List: [1, 2, 3, 4, 5]
Reversed List: [5, 4, 3, 2, 1]
```

---

## Key Concepts Demonstrated
- Singly Linked List structure.
- In-place reversal of a linked list.
- Algorithmic complexity analysis.
