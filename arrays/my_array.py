"""
my_array.py

A simple, fixed-size array built from scratch to teach how arrays work.

Key ideas for students:
    1. An array has a FIXED capacity (here: 5 slots). It cannot grow.
    2. Every slot starts with a default value (here: 0).
    3. We keep track of how many slots are filled using `current_index`.
    4. Inserting at the start or in the middle means SHIFTING elements
       to the right to make room. That is why those inserts are slower
       (O(n)) than inserting at the end (O(1)).
"""


class MyArray:
    """A fixed-size array that supports insert-at-start, insert-at-end
    and insert-at-position operations."""

    DEFAULT_CAPACITY = 5

    def __init__(self, length=DEFAULT_CAPACITY):
        """
        Create an array of `length` slots, all initialised to 0.

        Instance variables:
            length        -> total capacity of the array (number of slots)
            array         -> the storage itself, e.g. [0, 0, 0, 0, 0]
            current_index -> the position where the NEXT element will go.
                             It also equals the number of filled slots.
                             0 means the array is empty,
                             `length` means the array is full.
        """
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Array length must be a positive whole number.")

        self.length = length
        self.array = [0] * length
        self.current_index = 0

    # ------------------------------------------------------------------
    # Helper methods
    # ------------------------------------------------------------------
    def is_full(self):
        """Return True when every slot is already used."""
        return self.current_index == self.length

    def is_empty(self):
        """Return True when no element has been inserted yet."""
        return self.current_index == 0

    def _shift_right_from(self, position):
        """
        Move every element from `position` up to the last filled slot
        one step to the right, opening a free slot at `position`.

        We walk BACKWARDS (from the end towards `position`) so that we
        never overwrite a value before it has been copied.

        Example: shift right from position 1
            before: [10, 20, 30, 0, 0]   current_index = 3
            after : [10, 20, 20, 30, 0]  (slot 1 is now free to overwrite)
        """
        for i in range(self.current_index, position, -1):
            self.array[i] = self.array[i - 1]

    # ------------------------------------------------------------------
    # Insert operations
    # ------------------------------------------------------------------
    def insert_at_end(self, value):
        """
        Insert `value` right after the last filled element.
        Time complexity: O(1) - no shifting needed.

        Returns True if inserted, False otherwise.
        """
        # Edge case: no free slot left.
        if self.is_full():
            print(f"Cannot insert {value} at end: array is full.")
            return False

        self.array[self.current_index] = value
        self.current_index += 1
        return True

    def insert_at_start(self, value):
        """
        Insert `value` at index 0, pushing existing elements to the right.
        Time complexity: O(n) - every element may need to shift.

        Returns True if inserted, False otherwise.
        """
        # Inserting at the start is just inserting at position 0.
        return self.insert_at_position(0, value)

    def insert_at_position(self, position, value):
        """
        Insert `value` at `position`, shifting later elements to the right.

        Valid positions are 0 .. current_index (inclusive):
            - 0              -> same as insert at start
            - current_index  -> same as insert at end
        Positions beyond current_index are rejected because they would
        leave an empty "gap" in the array, which arrays do not allow.

        Time complexity: O(n) in the worst case.

        Returns True if inserted, False otherwise.
        """
        # Edge case 1: position must be a whole number.
        if not isinstance(position, int):
            print(f"Cannot insert {value}: position must be an integer, "
                  f"got {position!r}.")
            return False

        # Edge case 2: no free slot left.
        if self.is_full():
            print(f"Cannot insert {value} at position {position}: "
                  f"array is full.")
            return False

        # Edge case 3: position out of the valid range.
        if position < 0 or position > self.current_index:
            print(f"Cannot insert {value} at position {position}: "
                  f"valid positions are 0 to {self.current_index}.")
            return False

        # Step 1: make room by shifting elements to the right.
        self._shift_right_from(position)

        # Step 2: place the new value in the freed slot.
        self.array[position] = value

        # Step 3: one more slot is now in use.
        self.current_index += 1
        return True

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------
    def print_elements(self):
        """
        Print every slot with its index and value, and show where
        `current_index` is pointing.

        Filled slots are marked "(filled)", unused ones "(empty)".
        """
        print("-" * 36)
        print(f"{'Index':<8}{'Value':<10}Status")
        print("-" * 36)

        for index in range(self.length):
            status = "(filled)" if index < self.current_index else "(empty)"
            pointer = "  <-- current_index" if index == self.current_index else ""
            print(f"{index:<8}{self.array[index]:<10}{status}{pointer}")

        print("-" * 36)
        print(f"Length (capacity) : {self.length}")
        print(f"Current index     : {self.current_index}")
        print(f"Elements stored   : {self.current_index}")
        if self.is_full():
            print("Status            : FULL (current_index is past the last slot)")
        elif self.is_empty():
            print("Status            : EMPTY")
        print()
