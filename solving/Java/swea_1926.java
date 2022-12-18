import java.util.Scanner;

public class swea_1926 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		for (int i = 1; i < N + 1; i++) {
			String game = String.valueOf(i);
			int count = 0;
			for (int index = 0; index < game.length(); index++) {
				if (game.charAt(index) == '3' || game.charAt(index) == '6' || game.charAt(index) == '9') {
					count ++;
				}
			}
			if (count > 0) {
				for (int j = 0; j < count; j ++) {
					System.out.print('-');
				}
				System.out.print(' ');
			}
			else {
				System.out.printf("%d ", i);
			}
			
		}
	}

}
