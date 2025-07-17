
public class BasicTypeEx {
	public static void main(String[] args) {
		//Systemがオブジェクト、outが変数
		System.out.println("Hello");
		
		
		//정수형 : 암목적으로 int 기본
		int x = 0;
		
		
		//실수형 : 명시적으로 default 타입 double
		double d = 0.1;
		float f = 0.1f;
		
		
		//문자형 : char
		char c = 'A';
		System.out.println(c);
		c = 66;
		System.out.println(c);
		
		
		//boolean type
		boolean boo = true;
		
		String str = new String("ABC");
		str.equals(str);
		
		// "="의 의미
		int xx = 10;
		int yy = 100;
		//xx의 값은? => 여전히 10
		
		int[] x1 = {10, 20, 30};
		int[] y1 = x1;
		y1[0] = 100;
		//x1[0]의 값은? => 100
	}
}
