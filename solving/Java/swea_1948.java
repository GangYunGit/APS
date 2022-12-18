import java.util.Scanner;

public class swea_1948 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] month_info = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		int T = sc.nextInt();
		
		for (int test_case = 1; test_case < T + 1; test_case++) {
			int m1 = sc.nextInt();
			int d1 = sc.nextInt();
			int m2 = sc.nextInt();
			int d2 = sc.nextInt();
			
			int month_calculate = 0;
			int day_calculate = 0;
			for (int i = m1; i < m2; i++) {
				month_calculate = month_calculate + month_info[i];
			}
			day_calculate = d2 - d1 + 1;
			System.out.printf("#%d %d\n", test_case, month_calculate + day_calculate);
		}

	}

}
