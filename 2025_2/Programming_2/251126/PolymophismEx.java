
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
	public void printA() { // method overriding : printA를 초기화
		System.out.println("C class 안의 printA()");
	}
	
	public void printC(){
		System.out.println("C");
	}
}



public class PolymophismEx {
	public static void main(String[] args) { // 한 번만 실행하는 method
		// 1)
		A a = new A(); // 객체화 = 메모리 올라감
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
		
		// 1)
		C c = new C();
		c.printC();
		c.printA();
		
		// 2-1)
		A cc = new C();
//		cc.printC(); // 여거 안되
		cc.printA();
		
		// 다형성
		System.out.println("--------------------");
		aa.printA(); // aa, cc : 같은 타입을 가지고 있는 타입인데
		cc.printA(); // 결과가 다르게 출력 = 다형성
		
		// 다형성 문법 적용의 조건
		// 1) class가 상속관계에 있어야 함
		// 2) method overriding이 필요함
		// 3) A aa = new B();
		
	}
}