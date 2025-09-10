
// 생성자를 사용하는 가장 큰 목적? 생성자는 도대체 어떤 용도로 사용하나??
// => 멤버변수 초기화!!
class MyCon{
	private int age;
	private String name;
	
	public MyCon() {
		age = 20;
		name = "김길동";
	}
	
	public MyCon(int a, String n) { // default 생성자는 아나다
		this(n, a); // 생성자 호출
//		age = a;
//		name = n;
	}
	
	public MyCon(String n, int a) {
		age = a;
		name = n;
	}
	
	// default constructor
//	public MyCon() {
//		System.out.println("생성자 호출");
//	}
}

public void setAge(int a) {
	if (a < 150) {
		age = a;
	}
}

public String getName() {
	return name;
}

public class ConstructorEx {
	public static void main(String[] args) {
		MyCon m1 = new MyCon(20, "김길동"); // 새ㅇ성자 호출 -> 객체 생성
		m1.age = 22;
//		m1.setAge(22);
		System.out.println(m1.name);
		
		MyCon m2 = new MyCon(22, "박길동");
		
		
	}
}
