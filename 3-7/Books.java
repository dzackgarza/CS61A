
public class Books {

	public static void main(String[] args) {

		float chargePerBook = 299;
		float book1 = 1688, book2 = 2315, book3 = 1700;

		float total = (book1 + book2 + book3) + (3 * chargePerBook);

		System.out.println("The total is: " + total / 100 + " dollars.");

	}
}
