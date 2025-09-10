
// 

class AAA extends Object{
	public AAA() {
		System.out.println("내가 AAA 상성자");
	}
}

class BBB extends AAA{
	public BBB() {
		super();
		System.out.println("내가 BBB 상성자");
	}
}

public class OOPEx2 {
	public static void main(String[] args) {
		AAA a = new BBB();
		
		// new BBB();

	}
}