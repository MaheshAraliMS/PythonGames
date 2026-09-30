public class MyArray {

    int[] array;       // stores the elements
    int length;        // total size of the array
    int currentIndex;  // next free position (also = number of elements)

    public MyArray() {
        length = 5;
        array = new int[length];  // Java fills it with 0 by default
        currentIndex = 0;
    }

    // Insert at the end
    public void insertAtEnd(int value) {
        if (currentIndex == length) {
            System.out.println("Array is full. Cannot insert " + value);
            return;
        }
        array[currentIndex] = value;
        currentIndex++;
    }

    // Insert at the start
    public void insertAtStart(int value) {
        if (currentIndex == length) {
            System.out.println("Array is full. Cannot insert " + value);
            return;
        }
        // shift all elements one step to the right
        for (int i = currentIndex; i > 0; i--) {
            array[i] = array[i - 1];
        }
        array[0] = value;
        currentIndex++;
    }

    // Insert at a given position
    public void insertAtPosition(int position, int value) {
        if (currentIndex == length) {
            System.out.println("Array is full. Cannot insert " + value);
            return;
        }
        if (position < 0 || position > currentIndex) {
            System.out.println("Invalid position " + position
                    + ". Valid positions are 0 to " + currentIndex);
            return;
        }
        // shift elements from position onwards one step to the right
        for (int i = currentIndex; i > position; i--) {
            array[i] = array[i - 1];
        }
        array[position] = value;
        currentIndex++;
    }

    // Print index and value of every element
    public void printElements() {
        System.out.println("Index\tValue");
        for (int i = 0; i < length; i++) {
            System.out.println(i + "\t" + array[i]);
        }
        System.out.println("Current index: " + currentIndex);
        System.out.println();
    }
}
