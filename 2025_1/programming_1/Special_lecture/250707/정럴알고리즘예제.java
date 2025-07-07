
class Sor{
	//두개의 정수값을 전달받아서 가장 큰값 리턴하는 메소드
	public int max(int x, int y) {
		int result = 0;
		if (x > y) {
			result = x;
		}else {
			result = y;
		}
		return result;
	}
	public void 지정된값배열에서초기화() {
		
	}
}

public class 정럴알고리즘예제 {
	public static void main(String[] args) {
//		int[] x = {20, 130, 90, 50, 10};
		int[] x = {8, 7, 5, 1, 3, 6};
		
		// x[0], x[1] 값 비교해서 큰 값 출력, max 메소드 사용할것
		Sor s = new Sor();
		int r = 0; // Java에서 멤버변수는 자동초기화 지원 되지만, 지역변수는 초기화
		for (int i = 0; i < x.length; i++) { // x.length: 개수
			r = s.max(r, x[i]); // 비교해서 큰 값을 return
		}
		System.out.println(r);		

		
		// 배열 x에서 두번째로 큰 값 찾아내기
		// 1) 제일 큰 값 찾아내기
		// 2) 제일 큰 값을 없애버리기(0으로 변경)
		for (int i = 0; i < x.length; i++) {
			if (x[i] == r) { // x[0]가 방금전에 찾은 제일 큰 값(r)인가?
				x[i] = 0;
			}
		}
		
		// 3) 배열에서 제일 큰값 다시 찾으면 그 값이 두번 큰값
		r = 0;
		for (int i = 0; i < x.length; i++) {
			r = s.max(r, x[i]);
		}
		System.out.println(r);
	
		
		// 배열 x에서 세번째로 큰 값 찾아내기
		// 1) 제일 큰 값 찾아내기
		// 2) 제일 큰 값을 없애버리기(0으로 변경)
		for (int i = 0; i < x.length; i++) {
			if (x[i] == r) { // x[0]가 방금전에 찾은 제일 큰 값(r)인가?
				x[i] = 0;
			}
		}
		
		// 3) 배열에서 제일 큰값 다시 찾으면 그 값이 두번 큰값
		r = 0;
		for (int i = 0; i < x.length; i++) {
			r = s.max(r, x[i]);
		}
		System.out.println(r);
	}

}
