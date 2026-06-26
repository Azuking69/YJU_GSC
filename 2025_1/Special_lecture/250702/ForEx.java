
public class ForEx {
	public static void main(String args[]) {
		// 반복문 사용
		// Java에서는 반복문 작성을 위해 for문법을 사용
		// for(초기값 설정: 반복 조건 : 증감식){반복될 코드}		
		for (int i=0; i < 10; i++) {
			System.out.println(i);
		}
		
		// 1~10까지 누적 합계를 더해서 결과를 출력하는 코드를 작성하세요.
		// 조건 : 반복문을 사용해서
		int result = 0;
		for (int i = 0; i <= 10; i++) {
			result = result + i;
		}
		System.out.println(result);
		
		// 정수 1을 10번 누적해서 더한 결과를 출력하세요.
		// 조건 : 반복문 사용
		int result2 = 0;
		for (int i = 0; i < 10; i++) {
			result2 = result2 + 1;
		}
		System.out.print("result2=" + result2);
		
		// 내 답
		int resule_2 = 0;
		int num = 1;
		for (int j = 0; j <= 9; j++) {
			resule_2 = resule_2 + num;
		}
		System.out.print(resule_2);
		
		// 조건 : 실수0.1을 10번 누적해서 더한 결과를 출력하세요.
		double result3 = 0;
		double k = 0.1;
		for (int i = 0; i < 10; i++) {
			// 실수 산술 연산의 경우 결과 오자 발생
			// 실수
			// 
			
			result3 = result3 + k;
		}
		System.out.print("result3=" + result3);
		
	}

}