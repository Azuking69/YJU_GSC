
class Person{
	
}

public class 나의저장공간 extends Object { // Object o = new String("딸기");
										// Object o = new Person();
	// 나의저장공간 데이터를 저장하기 위한 메소드
	public void push (Object o) {
		
	}
//	public void push(String str) {
//			
//	}
//	
//	public void push(Person p) {
//		
//	}
		
	// 나의저장공간 데이터를 저장하기 위한 메소드
	public Object pop() {
//		return "ABC"
		return new Person();
	}
	
	public String pop() {
			return "default";
	}
	
	public String pop() {
		return new Person();
}
	
	
	public static void main(String[] args) {
		나의저장공간 a = new 나의저장공간();
		String r = a.pop();
		System.out.println(r);
		a.push("딸기");
	
			
	}
}