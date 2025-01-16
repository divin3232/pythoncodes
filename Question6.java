public class Question6 {
    
	public static void main(String[] args) {
        int[] big = {8,7,4,5,9,3,2};
        int largest = big[0];
        int indexSmall = 0;

        for (int i = 1; i < big.length; i++) {
            if (big[i] > largest) {
                largest = big[i];
                indexSmall = i;
            } else if (big[i] == largest && i < indexSmall) {
                indexSmall = i;
            }
        }

        System.out.println("The smallest index: " + indexSmall);
    }
}