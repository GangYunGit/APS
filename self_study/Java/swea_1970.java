import java.util.Scanner;

public class swea_1970 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int i = 1; i < T + 1; i ++) {
			
			int[] money_info = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
			int[] arr = new int[8];
			int N = sc.nextInt();
			for (int j = 0; j < 8; j ++) {
				if  ((N / money_info[j]) > 0) {
					arr[j] = N / money_info[j];
					N = N % money_info[j];
				}
				else {
					arr[j] = 0;
				}
			}
			System.out.printf("#%d\n", i);
			for (int k = 0; k < 8; k ++) {
				System.out.printf("%d ",arr[k]);
			}
			System.out.println();
				
		}

	}

}
