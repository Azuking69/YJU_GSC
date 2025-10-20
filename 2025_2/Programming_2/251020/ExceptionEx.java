
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
		
		int k[] = new int[3];
		k[0] = 0;
		k[1] = 10;
		k[2] = 100;
		try{
			System.out.println(k[3]);
		}catch (ArrayIndexOutOfBoundsException e){
			System.out.println("배열범위넘어가는 오류 발생");
			System.out.println(e);
//			e.printStackTrace();
		}
		
		try {
			int x1 = 10; 
			int x2 = 2;
			int r2 = x1 / x2; // new ArithmeticException();
			
			int xx1[] = {10, 20, 30};
			System.out.println(xx1[3]);
			// Exception e = new ArithmeticException();
			// Exception e = new ArrayIndexOutOfBoundsException();

		}catch (Exception e) { 
			System.out.println("Exception으로 통쳐내기");
			System.out.println(e);
		} finally {
			// 예외 발생 여부와 상관없이 무조건 실행
		}
		
//		} catch(ArrayIndexOutOfBoundsException e) {
//			
//		} catch(ArithmeticException e) {
//			
//		}
		
		System.out.println("end");
	}
}