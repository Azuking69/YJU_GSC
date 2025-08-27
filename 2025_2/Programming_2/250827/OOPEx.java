// class 구성요소 3가지
// 1. 멤버변수
// 2. 메소드
// 3. 생성자

// 자바 프로그램은 모든 코드를 class를 만들고 내부에 작성해야 함 
class MyClass {
	int x = 10; // 멤버변수
	// 멤버변수 선어 이외의 코드는 전부 메소드 안에 작성
	public void printX() {
		System.out.println(x);
		// y = 200; y변수는 printY()메소드 안에서만 쓸수 있는 지역변수
	}
	
	public void printY() {
		x = 100;
		System.out.println(x);
		int y = 20; // 지역변수 : 현대 메소드 안에서만 사용가능
	}
	
}

public class OOPEx {
	public static void main(String[] args) {
		// 자바 코드를 실행시키면 제일 먼저 실행되는 메소드는 main() 메소드!
		
		// printX()메소드 실행(호출)
		 MyClass m = new MyClass(); // Myclass를 메모링에 오려라
		 m.
		 printX();
	}

}
