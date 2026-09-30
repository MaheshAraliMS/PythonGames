public class ArrayDemo {

    public static void main(String[] args) {
        MyArray myArray = new MyArray();

        System.out.println("Initial array:");
        myArray.printElements();

        myArray.insertAtEnd(10);
        myArray.insertAtEnd(20);
        System.out.println("After inserting 10 and 20 at the end:");
        myArray.printElements();

        myArray.insertAtStart(5);
        System.out.println("After inserting 5 at the start:");
        myArray.printElements();

        myArray.insertAtPosition(2, 15);
        System.out.println("After inserting 15 at position 2:");
        myArray.printElements();

        // invalid positions
        myArray.insertAtPosition(-1, 99);
        myArray.insertAtPosition(7, 99);

        myArray.insertAtPosition(4, 25);
        System.out.println("After inserting 25 at position 4 (array is now full):");
        myArray.printElements();

        // array is full, all of these should fail
        myArray.insertAtEnd(30);
        myArray.insertAtStart(1);
        myArray.insertAtPosition(2, 50);
    }
}
