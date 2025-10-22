
// 자바에서 Thread 사용을 위한 문법 2가지
// 1)번 반식으로 정의
class MyThread1 extends Thread{
	public void run() {
		// Thread가 수행할 작업을 코딩
		for (int i = 0; i < 10; i++) {
			System.out.println(i);
		}
	}
}

public class ThreadEx {

	public static void main(String[] args) {
		// 1) 방식 사용
		MyThread1 m1 = new MyThread1();
		m1.run();

	}

}
