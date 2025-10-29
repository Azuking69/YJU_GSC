

// 프로적트 진행하다 보면 현재 프로잭트 정책상
// 예외 취급해야 되는 특정 상황 / 특정 코드가 생기게 됨
// 이런 우리만의 예외 상황을 관리하기 위해 우리만의 커스텀된 예외 클래스를 정의해 줄 수 있다

// 우리만의 예외를 정의해 줄 때에는 잡바의 룰에 따라 모든 예외 처리에 관련된 클래스의 
// 최상위 클래스에 해당하는 Exception 클래스를 상속 받도록 해야 함!
class MyExceotipn extends Exception{
	
}


public class CustomExceptionEx {
	public static void main(String[] args) {
		// 자 그럼 우리만의 예외 처리 클래스를 실제 사용해 보자
		try {
			int x = 10;
			int y = 0;
			int r = x / y;
			System.out.println(r);
		} catch (Exception e) {
			System.out.println("문제 발생");
		}
		

	}
}