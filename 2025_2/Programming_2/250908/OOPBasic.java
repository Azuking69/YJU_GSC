
// OOP : 유지보수 관리한 프로그램
// OOP에 출발점은
// 멤버변수 private 선어 부터
// 추가로 public getXXX / setXXX 메소드 구현

class MyStudents{
	public int age; // OOP 관점에 잘 못 된 코드
	private String name; // OOP 관점에 잘 못 된 코드
	
	public void setName(String n) {
		name = n;
	}
}


public class OOPBasic {
	public static void main(String[] args) {
		MyStudents m1 = new MyStudents();
		m1.age = 20;
		m1.name = "김길동"; // 이름 저장의 정첵이 바꿜 때 수정하러 다녀야함
		
		MyStudents m2 = new MyStudents();
		m2.age = 22;
		m2.name = "박길동";
	}

}