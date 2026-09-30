"""
array_demo.py

Creates a MyArray object and walks through every insert operation,
including the edge cases, printing the array after each step.

Run with:
    python array_demo.py
"""

from my_array import MyArray


class ArrayDemo:
    """Drives MyArray step by step so students can watch it change."""

    def __init__(self):
        self.my_array = MyArray()  # capacity 5, all zeros

    def show(self, title):
        """Print a heading followed by the current state of the array."""
        print(f"=== {title} ===")
        self.my_array.print_elements()

    def run(self):
        # 1. Freshly created array: all zeros, current_index = 0.
        self.show("Initial array")

        # 2. Insert at end: fills slots left to right, no shifting.
        self.my_array.insert_at_end(10)
        self.my_array.insert_at_end(20)
        self.show("After insert_at_end(10) and insert_at_end(20)")

        # 3. Insert at start: 10 and 20 shift one step right.
        self.my_array.insert_at_start(5)
        self.show("After insert_at_start(5)")

        # 4. Insert in the middle: 10 and 20 shift, 15 goes to index 2.
        self.my_array.insert_at_position(2, 15)
        self.show("After insert_at_position(2, 15)")

        # 5. Edge cases for position (array is NOT full yet).
        print("=== Edge cases: invalid positions ===")
        self.my_array.insert_at_position(-1, 99)   # negative index
        self.my_array.insert_at_position(7, 99)    # would leave a gap
        self.my_array.insert_at_position("2", 99)  # not an integer
        print()

        # 6. Insert at position == current_index behaves like insert at end.
        self.my_array.insert_at_position(4, 25)
        self.show("After insert_at_position(4, 25) - array is now full")

        # 7. Edge cases: every insert must fail on a full array.
        print("=== Edge cases: array is full ===")
        self.my_array.insert_at_end(30)
        self.my_array.insert_at_start(1)
        self.my_array.insert_at_position(2, 50)
        print()

        self.show("Final array (unchanged by failed inserts)")


if __name__ == "__main__":
    ArrayDemo().run()
