// 자바에서 메소드 정의 문법
// 접근제한자 리턴현 메소드이름(파라미터){실제코드...}

// 접근제한자 종류: public protected default private
//              public : 누구나 접근해서 사용가능 메소드
//              private : 메소드가 정의된 클래스 안에서만 사용가능

// 리턴형 종류: 기본자료형, 객체형, void(리턴형이 없음을 의미)

class MyCal {
	// 정수 덧셈 가능을 하는 메소드 구현
	public int add(int x, int y) {
		int r = x + y;
		return r;
	}
	// 실수 덧셈 가능을 하는 메소드 구현
	public double add(double x, double y) {
		double r = x + y;
		return r;
	}
}


class 라면집{
	//	public(접근제한자) void(리턴형) 라면끓어줘(메소드이름)
	public void 라면끓어줘(int 라면살돈) { // 메소드 정의
		// 라면 제작을 위한 프로그래밍
		// ...
		System.out.println("세우탕");
		
	}
}

public class MethodEx {
	public static void main(String[] args) {
		
		MyCal m = new MyCal();
		int result = m.add(1, 2);
		System.out.println(result);
		
		double result2 = m.add(0.1, 0.2);
		System.out.println(result2);
		
		MyCal m1 = new MyCal();
		double result1 = m1.add(1, 2);
		System.out.println(result1);
		
		
		// 라면끓어줘 메소드 사용(호출)
		// 메소드 호출: 메소드 이름을 사용하여 호출 가능
		// 1. 해당 메소드를 가지고 있는 클래스 객체화
		// 2. 객체이름, 메소드이름(파라미터);
		
		// 1. 라면끓어줘 메소드를 가지고 있는 클래스 객체화
		라면집 a = new 라면집();
		// 2. 객체이름, 메소드이름(파라미터);
		a.라면끓어줘(1000);
		


	}

}
