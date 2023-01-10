import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String N = br.readLine();
		int[] placeNum = new int[9];
		for(int i = 0; i < 9; i++) {
			if(i == 0) {
				placeNum[i] = 0;
			} else {
				placeNum[i] = 9 * i * (int)Math.pow(10, i - 1);
			}
		}
		int numLength = N.length();
		int result = 0;
		for(int i = 0; i < numLength; i++) {
			result += placeNum[i];
		}
		int valueOfN = Integer.valueOf(N);
		result += (valueOfN - (int)Math.pow(10, numLength - 1) + 1) * numLength;
		System.out.println(result);
	}
}