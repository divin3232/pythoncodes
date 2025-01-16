import java.util.*;
public class Question3 {

	public static void main(String... sad) {
	
	Scanner snack = new Scanner(System.in);
	
	
	System.out.println("Enter a number:");
	int number = snack.nextInt();
	
	System.out.println("The factor of " + number + " are:");

for (int count = 1; count < number;	count++) {

	if (number % count == 0) {
		System.out.println(count);
	
	}

}
	
	
	
	}


}