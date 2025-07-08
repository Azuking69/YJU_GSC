
class A{
	public A() {
		System.out.println("A 생성자 호출");
	}
}
class B extends A{
	public B() {
		System.out.println("B 생성자 호출");
	}
}


public class Test {
	public static void main(String[] args) {
		A a = new B(); // 됨
//		B b = new A(); // 안됨

	}

}