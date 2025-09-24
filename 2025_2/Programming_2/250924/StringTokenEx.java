import java.util.StringTokenizer;

public class StringTokenEx {
	public static void main(String args[]) {
		// StringTokenizer : 문자열 분리를 위해 사용하는 클래스
		
		String str = "3 + 2 + 1";
		
		StringTokenizer t = new StringTokenizer(str, "+");
		String r = t.nextToken();
		System.out.println(r);
		r = t.nextToken();
		System.out.println(r);
		r = t.nextToken();
		System.out.println(r);
	}
}
