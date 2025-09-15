// 자바에서 3가지 생략 가능한 주요문법이 존재
// (1)extends Object : 모든 클래스는 object 클래스를 상속받고 있다
//                     자바 클래스의 최상위 클래스는 Object class 다
// (2)Default constructor : 
//                          개발자가 생성자를 하나도 만들어주지 많으면
//                          디펄트 생성자는 자동으로 만들어짐
// (3)super(); : 모든 
//               상위 클래스 디펄트 생성자 호출을 의미

class SuperA extends Object{
	
}

class MyA extends SuperA{
	public MyA() { // 파라미터를 받지 않는 디펄트 생성자 생략 가능
		super(); // 생략 가능
	}
	
}


public class 삼대생략요소 {
	public static void main(String[] args) {
		

	}
}