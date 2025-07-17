import java.util.StringTokenizer;

public class WhileEx {
	public static void main(String[] args) {
		int result = 0;
		for (int i = 1; i < 10; i++) {
			result = result + i;
		}
		
		
		String str = "3 + 1 + 2 + 4";
		StringTokenizer st = new StringTokenizer(str, "+");
		
		while(st.hasMoreTokens()) {
			String r = st.nextToken(); //분리된 값 가져오기
			System.out.println(r);
		}
	}
}