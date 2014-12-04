
import java.util.Scanner;

public class HelloWorld {

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		String first, last, full;
		System.out.println("Hello, world");
		
		System.out.println("What's your first name?");
		first = input.nextLine();
		
		System.out.println("What's your last name?");
		last = input.nextLine();

		full = first + ' ' + last;

		System.out.println("Hello, " + full);
	}
}
