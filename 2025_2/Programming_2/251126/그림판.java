
class 그림판UI{
	// JButton 동그라미버튼;
	// ...
	
	// 아래 여러 도형을 그리는 메소드를 하나로 통쳐보자
	// 아래 각 도형 내용을 변경해도 여긴 바꾸지 않아도 됨
	public void 도형버튼클릭해서그리기(도형 x) { // [= new 삼각형();], [= new 동그라미();]
		
	}
	
	// 아래 코드를 다형성 문법을 사용해서 하나로 통쳐내갰다.
//	public void 동그라미버튼클릭해서그리기(동그라미 x) {
//		//...
//		x.그리기();
//	}
//	
//	public void 삼각형버튼클릭해서그리기(삼각형 x) {
//		x.그리기();
//	}
//	
//	public void 네모버튼클릭해서그리기(네모 x) {
//		x.그리기();
//	}
//	
//	public void 오각형버튼클릭해서그리기(오각형 x) {
//		x.그리기();
//	}
}

abstract class 도형{ // 추상화 class
	abstract public void 그리기();
}

class 동그라미 extends 도형{ // 아이1
	public void 그리기() {
		System.out.println("동그라미가 그려지고 있다.");
	}
}

class 삼각형 extends 도형{ // 아이2
	public void 그리기() {
		System.out.println("삼각형 그려지고 있다.");
	}
}

class 네모 extends 도형{ // 아이3
	public void 그리기() {
		System.out.println("네모가 그려지고 있다.");
	}
}

class 오각형{ // 아이4
	public void 그리기() {
		System.out.println("오각형 그려지고 있다.");
	}
}


public class 그림판 {
	public static void main(String[] args) {
		그림판UI u = new 그림판UI();
		
		u.도형버튼클릭해서그리기(new 동그라미());
		u.도형버튼클릭해서그리기(new 삼각형());
		u.도형버튼클릭해서그리기(new 네모());
	}
}