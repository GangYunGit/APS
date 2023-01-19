import java.util.HashSet;

public class Main {
	public static int selfNumber(int n) {
		String splitNum = n + "";
		String[] arr = new String[splitNum.length()];
		arr = splitNum.split("");
		for(String val: arr) {
			n += Integer.valueOf(val);
		}
		return n;
	}
	public static void main(String[] args) {
		HashSet<Integer> arr = new HashSet<Integer>();
		for (int i = 1; i <= 10000; i++) {
			int inputNum = i;
			while (inputNum <= 10000) {
				inputNum = selfNumber(inputNum);
				arr.add(inputNum);
			}
		}
		for (int i = 1; i <= 10000; i++) {
			if (!arr.contains(i)) {
				System.out.println(i);
			}
		}
	}
}