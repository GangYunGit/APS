import java.util.Scanner;

public class Main {
	public static int func(int initialNum, int num, int count) {
		String beforeSplit = "";
		if (num < 10) {
			beforeSplit = "0" + Integer.toString(num);
		} else {
			beforeSplit = Integer.toString(num);
		}

		String a = beforeSplit.substring(0, 1);
		String b = beforeSplit.substring(1, 2);
		int newTemp = Integer.parseInt(a) + Integer.parseInt(b);
		String newTempStr = Integer.toString(newTemp);
		if (newTempStr.length() == 2) {
			newTempStr = newTempStr.substring(1, 2);
		}
		String newStr = b + newTempStr;
		int newNum = Integer.parseInt(newStr);
				
		if (initialNum != newNum) {			
			return func(initialNum, newNum, count + 1);
		} else {
			return count;
		}
	}
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		System.out.println(func(N, N, 1));
	}
}