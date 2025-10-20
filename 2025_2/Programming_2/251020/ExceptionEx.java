
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
			e.printStackTrace();
		}
		
		
		System.out.println("end");
	}
}