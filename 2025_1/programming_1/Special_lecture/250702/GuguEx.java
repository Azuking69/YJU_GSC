
public class GuguEx {
	public static void main(String args[]) {
		// 구구단 2단을 출력하는 코드를 만드세요.
		// 문제 해결 과정
		// 1)문제를 해결하기 위한 가장 쉬운 편한 코드로 작성
		System.out.println("2x1=2");
		System.out.println("2x2=4");
		System.out.println("2x3=6");
		System.out.println("2x4=8");
		System.out.println("2x5=10");
		System.out.println("2x6=12");
		System.out.println("2x7=14");
		System.out.println("2x8=16");
		System.out.println("2x9=18");

		// 2)중복되는 코드 제거
		for (int i = 1; i < 10; i++) {
			int r = 2 * i;
			System.out.println("2x" + i + "=" + r);
		}

		// 내 답
		int x = 2;
		for (int y = 1; y < 10; y++) {
			System.out.println(x + "x" + y + "=" + x * y);
		}

		// 3단을 출력하는 코드 작성
		for (int i = 1; i < 10; i++) {
			int r = 3 * i;
			System.out.println("3" + i + "=" + r);
		}

		// 내 답
		int a = 3;
		for (int b = 1; b < 10; b++) {
			int result = a * b;
			System.out.println(a + "x" + b + "=" + result);
		}

		// 4단을 출력하는 코드 작성
		for (int i = 1; i < 10; i++) {
			int result = 4 * i;
			System.out.println("4x" + i + "=" + result);
		}

		for (int i = 1; i < 10; i++) {
			int result = 5 * i;
			System.out.println("5x" + i + "=" + result);
		}

		for (int i = 1; i < 10; i++) {
			int result = 6 * i;
			System.out.println("6x" + i + "=" + result);
		}

		for (int i = 1; i < 10; i++) {
			int result = 7 * i;
			System.out.println("7x" + i + "=" + result);
		}

		for (int j = 1; j < 10; j++) {
			
			for (int i = 1; i < 10; i++) {
				int r = j * i;
				System.out.println(j + "x" + i + "=" + r);
			}
			System.out.println("---------------");
		}
		
	}

}
