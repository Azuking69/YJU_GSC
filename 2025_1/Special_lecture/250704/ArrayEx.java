
class Arm{
	int[] x;
	public void setArr(int[] xx) {
		x = xx;
		System.out.println("x[0] = " + x[0]);
	}
	
	// 가징 큰 값을 찾아주는 메소드
	public void getMax(int[] xx) {
		if (xx[0] > xx[1]) {
			// xx[0]가 xx[1]보다 크다
			if (xx[0] > xx[2]) {
				System.out.println("가징 큰 값 = " + xx[0]);
			}else {
				System.out.println("가징 큰 값 = " + xx[2]);
			}
		}else {
			// xx[1]가 xx[0]보다 크다
			if (xx[1] > xx[2]) {
				System.out.println("가징 큰 값 = " + xx[1]);
			}else {
				System.out.println("가징 큰 값 = " + xx[2]);
			}
		}
	}
}


// Java에서 배열 사용을 위한 문법 3까지
public class ArrayEx {
	public static void main(String[] args) {
		// Java에서 배열 사용을 위해 문법 3가지
		// 1)
		int[] x = new int[3];
		x[0] = 10;
		x[1] = 20;
		x[2] = 30;
		System.out.println(x[0]);
		
		// 2)
		int[] y = {10, 20, 30};
		System.out.println(y[0]);
		
		// 3)
		int[] k = new int[] {10, 20, 30};
		
		
//		int[] p = {10, 20, 30};
//		int[] q = p; // 同じ配列を共有
//		q[0] = 1000;
//		System.out.println(p[0]); // 출력: 1000
		
		Arm a = new Arm();
		a.setArr(x);
		a.setArr(k);
		a.setArr(new int[] {10, 20, 30});
		a.getMax(new int[] {1000, 200, 30});
		
	}
}
