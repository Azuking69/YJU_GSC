
// 자바에서 Thread 사용을 위한 문법 2가지
// 1)번 반식으로 정의
class MyThread1 extends Thread{
	public void run() { // callback method
		// Thread가 수행할 작업을 코딩
		for (int i = 0; i < 10; i++) {
			System.out.println(i);
		}
	}
}

// 2)번 방식
class Mythread2 implements Runnable{
	@Override
	public void run() {
		// Thread 수행할 작업을 코딩
		for(int i = 0; i < 10; i++) {
			System.out.println(i);
		}
	}
}

public class ThreadEx {
	public static void main(String[] args) {
		System.out.println("Start");
		// 1) 방식 사용
		MyThread1 m1 = new MyThread1();
		m1.start(); // Thread 실행을 위해서는 꼭! start()메서드 호출할 것!
//		m1.run(); // 잘못된 코드
		
		// 2) 방식 사용
		Mythread2 m2 = new Mythread2();
		Thread m2t = new Thread(m2);
		m2t.start(); 
		// start() 메소드 호출이 이제 Thread 실행을 의미하는 것은 아니다.
		// 해당 Thread가 CPU 제어권을 얻을 수 있는 대비방에 들어가게 됨을 의ㄴ미
		
		System.out.println("End");
	}

}
