
// 변수 : 변하는 값을 저장하기 위한 공간
// 멤버변수(member variable)
//	:클래스 전체에서 사용가능한 변수, 클래스의 멤버다 
// 지역변수(local variable)
//　:특정지역(ex:메소드)에서만 사용가능한 변수

public class VariableEx {
	static int x  =10; // member variable
	
	public static void main(String[] args) {
		
		new VariableEx();
		
		int y = 100; // local variable
		y = 200;
		System.out.println(y);
		
//		VariableEx v = new VariableEx();
//		System.out.println(v.x);
		
		System.out.println(x);

	}

}
