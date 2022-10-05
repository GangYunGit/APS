import java.util.Scanner;

public class swea_2007 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for (int i = 1; i <= T; i++) {
			String my_str = sc.next();
			for (int idx = 1; idx <= my_str.length(); idx++) {
				if (my_str.substring(0, idx).equals(my_str.substring(idx, idx*2))) {
					System.out.printf("#%d %d\n", i, idx);
					break;
				}
			}
		}
	}
}
