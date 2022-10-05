import java.util.Scanner;

public class swea_1288 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for (int i = 1; i < T + 1; i++) {
			int k = 1;
			int N = sc.nextInt();
			int[] counter = new int[10];
			
			while (true) {
				String sheep = N * k + ""; 
				for (int j = 0; j < sheep.length(); j++) {
					char temp = sheep.charAt(j);
					int num_temp = (int)temp - 48;
					counter[num_temp] = 1;
				}
				k++;
				int cnt = 1;
				for (int a = 0; a < 10; a++) {
					cnt = counter[a] * cnt;
				}
				if (cnt == 1) break;
			}
			System.out.printf("#%d ", i);
			System.out.println((k - 1) * N);
		}
	}
}
