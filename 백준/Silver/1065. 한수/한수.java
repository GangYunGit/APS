import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int count = 0;
		for(int i = 1; i <= N; i++) {
			if(i < 100) {
				count++;
			} else {
				String num = (i + "");
				ArrayList<Character> arr = new ArrayList<Character>();
				for(int j = 0; j < num.length(); j++) {
					arr.add(num.charAt(j));
				}
				boolean isHansu = true;
				for(int j = 0; j < num.length() - 2; j++) {
					if(arr.get(j + 1) - arr.get(j) != arr.get(j + 2) - arr.get(j + 1)) {
						isHansu = false;
						break;
					} 
				}
				if(isHansu) {
					count++;
				}
			}
			
		}
		System.out.println(count);
	}
}