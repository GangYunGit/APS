import java.util.Scanner;

public class swea_2001 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for (int test_case = 1; test_case < T + 1; test_case++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			int max_flies = 0;
			int[][] arr_flies = new int[N][N];
			for (int N_i = 0; N_i < N; N_i++) {
				for (int N_j = 0; N_j < N; N_j++) {
					arr_flies[N_i][N_j] = sc.nextInt();
				}
			}
			
			for (int i = 0; i <= N - M; i++) {
				for (int j = 0; j <= N - M; j++) {
					int sum_flies = 0;
					for (int M_i = 0; M_i < M; M_i++) {
						for (int M_j = 0; M_j < M; M_j++) {
							sum_flies = sum_flies + arr_flies[M_i + i][M_j + j];
						}
						
					}
					if (sum_flies > max_flies) {
						max_flies = sum_flies;
						
					}
				}
			}
			System.out.printf("#%d %d\n", test_case, max_flies);
		}
	}

}
