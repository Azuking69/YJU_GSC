
class MyPerson{
	int age = 20;
	String name = "김길동";
	int score1 = 90;
	int score2 = 80;
	int score3 = 70;
	int e = 0; // 평균값을 저장하기 위한 변수
	
	public void 성적평균구하기() {
		int result = score1 + score2 + score3;
		e = result / 3;
	}
	
	public void 성적표출력(){
		System.out.println("이름: " + name);
		System.out.println("나이: " + age);
		System.out.println("성적편균: " + e);
	}
	
}

public class 성적평균구하기 {
	public static void main(String[] args) {
		MyPerson m1 = new MyPerson();
		m1.성적평균구하기();
		m1.성적표출력();
				
		
		MyPerson m2 = new MyPerson();
		m2.name = "박길동";
		m2.age = 20;
		m2.score1 = 100;
		m2.score2 = 100;
		m2.score3 = 90;
		
		m2.성적평균구하기();
		m2.성적표출력();
	}
}
