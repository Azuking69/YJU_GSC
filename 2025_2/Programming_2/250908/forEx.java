
// 다음과 같이 "*"를 사용하여 삼각형 모양에 출력 결과를 가칠 수 있도록
// for 문울 사용하여 코딩하시오
// *
// **
// ***
// ****
// *****

public class forEx {
	
	// x = x + 1 == x + 1
	// x++ == x + 1
	// ++x == x = x + 1
	public void printC(char c, int x) {
		System.out.println(c);
		if (x > 1) {
			System.out.print(x);
			printC(c, x-1);
		}
	}
	
	public static void main(String[] args) {	
		for (int j = 1; j < 10; j++){
			forEx f = new forEx();
			f.printC('*', j);
			System.out.println("");
		
		}
			
//		for (int j = 0; j < 10; j++){
//			for (int i = 0; i < j; i++) {
//				System.out.print("*");
//			}
//			System.out.println();
//		}
		
		
//		// 자바에서 반복문
//		// 기본적인 문법
//		// for (초기값; 조건식 증가식){반복할 코드}
//		 for (int i = 0; i < 10; i++) {
//			 System.out.println(i);
//		}

		
		
	}

}