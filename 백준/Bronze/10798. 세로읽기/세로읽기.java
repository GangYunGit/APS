import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<String>[] board = new ArrayList[5];
		
		for(int i = 0; i < 5; i++) {
			board[i] = new ArrayList<String>();
		}
		
		int maxCol = 0;
		for(int i = 0; i < 5; i++) {
			String colWords = sc.next();
			maxCol = Math.max(maxCol, colWords.length());
			for(int j = 0; j < colWords.length(); j++) {
				board[i].add(colWords.charAt(j) + "");
			}
		}
		
		for(int i = 0; i < maxCol; i ++) {
			for(int j = 0; j < 5; j++) {
				if (i < board[j].size()) {
					System.out.print(board[j].get(i));
				}
			}
		}
	}
}