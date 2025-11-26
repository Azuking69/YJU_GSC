
class A{ // class
	public void printA() { // method
		System.out.println("A"); // 실행 내용
	}
}

class B extends A{ // printA()를 가지고 있는 class
	public void printA() { // method overriding : printA를 초기화
		System.out.println("B class 안의 printA()");
	}
	
	public void printB() {
		System.out.println("B");
	}
}

class C extends A{
	public void printC(){
		System.out.println("C");
	}
}


public class PolymophismEx {
	public static void main(String[] args) { // 한 번만 실행하는 method
		// 1)
		A a = new A(); // 객체화
		a.printA(); // method 호출
		
		// 2)
		A aa = new B(); // class A의 상속을 받은 B
//		B bb = new A(); // class B의 상속을 받지 않는 A
		aa.printA();
//		aa.printB(); //이게 안된다아~!
		// 아니이 B class 안에 있는 메소드도 호출이 안되는데 뭐때문에 B class를 객체화하지?
		// A aa = new B(); <= 이 코드에 장점이 없잖아?
		// 결론부터 애기하자면 다현성을 사용하기 뮈해!!!
			
//		B b = new B();
//		b.printB();
//		b.printA(); // class B 안에 printA()가 있음
		
		C c = new C();
		c.printC();
	}
}