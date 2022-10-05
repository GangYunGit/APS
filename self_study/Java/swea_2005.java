import java.util.Scanner;

public class swea_2005 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
	
		for (int test_case = 1; test_case < T + 1; test_case++) {
			int N = sc.nextInt();
			int[][] arr = new int [N][N];
			for (int i = 0; i < N; i++) {
				if (i == 0) {
					arr[i][i] = 1;
				}
				else if (i == 1) {
					arr[i][0] = 1;
					arr[i][i] = 1;
				}
				else {
					for (int j = 1; j < N-1; j++) {
						arr[i][0] = 1;
						arr[i][i] = 1;
						arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j];
					}
				}
			}
			System.out.printf("#%d\n", test_case);
			for (int k = 0; k < N; k++) {
				for (int k2 = 0; k2 < k + 1; k2++) {
					System.out.print(arr[k][k2]);
					System.out.print(' ');
				}
				System.out.println();
			}
		}
		
	}
}

