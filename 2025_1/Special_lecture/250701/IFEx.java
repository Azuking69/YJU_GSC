
public class IFEx {
	
	public static void main(String args[]) {
//		//Java에서 제어문 사용
//		if (특정 조건이 만족 하면) {
//			실행
//		}else {
//			그렇지많다면 else 실행
//		}
		int x = 30;
		int y = 20;
		int k = 100;
		
		// &&, &, ||, | 연산자
		// &&, ||가 더 똑똑
		// ++, +=, -=
		// x++ => x = x+1;
		// x+=10 => x = x + 10;
		// x-=10 => x = x - 10;
		if (x > y && (k+=10) > 0) {
			System.out.println("조건 만족");
		}else {
			System.out.println("조건 불충");
		}
		System.out.println(k);
		
		// 스코어가 70이상일때 "C",
		// 80이상일때 "B",
		// 90이상일때 "A"를 출력하도록 코드 작성
		int score = 70;
		
		if (score >= 90) {
			System.out.println("A");
		}else if (score >= 80) {
			System.out.println("B");
		}else if (score >= 70) {
			System.out.println("C");
		}
		
//		if (score >= 70 && score < 80) {
//			System.out.println("C");
//		}else if (score >= 80 && score < 90){
//			System.out.println("B");
//		}else if (score >= 90 && score < 100) {
//			System.out.println("A");
		}
	}
}