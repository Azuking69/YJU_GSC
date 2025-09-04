
class MyPerson{
	int age;
	String name;
	int score1;
	int score2;
	int score3;
	
	int e = 0; // 평균값을 저장하기 위한 변수
	
	public MyPerson(String n, int a, int s1, int s2, int s3) {
		name = n;
		age = a;
		score1 = s1;
		score2 = s2;
		score3 = s3;
	}
	
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
		MyPerson m1 = new MyPerson("김길동", 20, 90, 80, 70);
		m1.성적평균구하기();
		m1.성적표출력();
				
		
		MyPerson m2 = new MyPerson("박길동", 20, 100, 100, 90);
		m2.성적평균구하기();
		m2.성적표출력();
		
		
		MyPerson m3 = new MyPerson("홍길동", 22, 90, 80, 90);
		m3.성적평균구하기();
		m3.성적표출력();
		
		
		// 전체 학생의 총점과 평균
		int totalScore = m1.score1 + m1.score2 + m1.score3
		+ m2.score1 + m2.score2 + m2.score3
		+ m3.score1 + m3.score2 + m3.score3;
		
		int totalE = totalScore / 9;
	}
}
