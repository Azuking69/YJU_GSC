// OOP 출발점
// 1. 모든 멤버변수 접근제한자 private

class MyPerson{
	// 클래스 전체에서 수로 쓰려고 정의
	int x1 = 0, x2 = 0, x3 = 0;
	
	// 계산
	public void 평균구하기(int x1, int x2, int x3) {
		int total = x1 + x2 + x3;
		double avg = total / 3;
		System.out.println(avg);
	}
}

public class 성적평균구하기 {
	public static void main(String[] args) {
		// 호출
		MyPerson m = new MyPerson();
		// 성적 점수
		m.x1 = 100;
		m.x2 = 90;
		m.x3 = 80;
		// 평균구하기 메소드 호출
		m.평균구하기(m.x1, m.x2, m.x3);
		
		// 호출
		MyPerson m2 = new MyPerson();
		// 성적 점수
		m2.x1 = 70;
		m2.x2 = 80;
		m2.x3 = 60;
		// 평균구하기 메소드 호출
		m.평균구하기(m2.x1, m2.x2, m2.x3);
		
	}
}