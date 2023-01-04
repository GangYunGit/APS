import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Character> checker = new ArrayList<Character>();
		
		int N = sc.nextInt();
		int count = N;
		for(int i = 0; i < N; i++) {
			String word = sc.next();
			for(int j = 0; j < word.length(); j++) {
				char ch = word.charAt(j);
				if(j > 0 && ch != checker.get(checker.size() - 1) && checker.contains(ch)) {
					count--;
					break;
				} else {
					checker.add(ch);
				}
			}
			checker.clear();
		}
		System.out.println(count);
	}
}