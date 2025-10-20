
public class ExceptionEx {
	public static void main(String[] args) {
		System.out.println("start");
		int x = 10;
		int y = 0;
		int r = 0;
		
		try {
			r = x / y;
			System.out.println(r); // r = x / y;에 오류가 없으면 출력
			
		} catch (ArithmeticException e) {
			// 예외를 잡아냈을 때 대용코드
			System.out.println("산술연산 오류 발생");
		}
		
		
		System.out.println("end");
	}
}