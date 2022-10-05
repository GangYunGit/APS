import java.util.Scanner;

public class swea_1976 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for (int i = 1; i <= T; i++) {
			int h_1 = sc.nextInt();
			int m_1 = sc.nextInt();
			int h_2 = sc.nextInt();
			int m_2 = sc.nextInt();
					
			int result_h;
			int result_m;
			if (h_1 + h_2 > 12) {
				result_h = h_1 + h_2 - 12;
			}
			else {
				result_h = h_1 + h_2;
			}
			if (m_1 + m_2 > 60) {
				result_m = m_1 + m_2 - 60;
				result_h++;
			}
			else {
				result_m = m_1 + m_2;
			}
			System.out.printf("#%d %d %d\n", i, result_h, result_m);
		}
	}
}
