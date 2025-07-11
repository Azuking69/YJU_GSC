
// Java에서 함수(메소드) 사용 방법
// 메소드 정의를 위한 문법
// 접근제한자 리턴형 메소드이름(파라미터){메소드호출시 실행할 코드}
// 접근제한자 : 누가 요놈을 쓸 수 있느냐
//          public = protected - default - private
//          public : 누구나 사용 가능
//          private : 나(class)만 사용 가능
// 리턴형 : 메소드 호출 결과값의 타입이 뭐냐
//        기본자료형, 객체형, void(리턴형이 없다 = 리턴값이 없다)
// 파라미터 : 메소드 호출시 던저주는 값

// 메소드 사용(호출)
// 메소드 호출을 위해서서는 메소드를 메모리애 올려주어야 한다
// 호출 문법 : 

class MyMethod{
	int age = 20;
	
	// 메소드 정의
	public void printA() { // 리턴형 없음(void)
		System.out.println("A");
	}
	
	public int getAge() { // 리턴형 int 타입으로 지정
		// 리턴형이 정의된 경우 "return" 사용하여 리턴값 넘겨줄것
		return age;
	}
}

public class MethodEx {
		public static void main(String args[]) {
			// 메소드 사용(호출)
			// 메소드를 메모리애 올려주기
			// Java에서는 메모리애 코드를 올려놓고 실행해줘야함
			
			// 메소드를 메모리에 올려주기 위해 메소드가 포함된 class를 통째 메모리에 올림
			MyMethod m = new MyMethod(); 
			m.printA(); // 메소드 사용(호출) 문법 : 메소드이름(파라미터값);
		    int age = m.getAge(); // 메소드 호출 결과로 넘어은 값 지정
		    System.out.println(age);
		}
}