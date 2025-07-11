
class MyCal{
	// 덧셈 기능을 하는 메소드 구현
	public void add(int x, int y) {
		int result = x + y;
		System.out.println(result);
	}
	
	// 실수 덧셈 기능을 하는 메소드 구현
	public void add_dd(double x, double y) {
		double result = x + y;
		System.out.println(result);
	}
}

public class MethodOverridingEx {
	public static void main(String args[]) {
		MyCal m = new MyCal(); // MyCal 객체화
		m.add(10, 20);
		m.add_dd(0.1, 0.2);
	}
}