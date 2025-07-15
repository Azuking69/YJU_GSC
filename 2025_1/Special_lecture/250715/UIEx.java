// ctrl + shift + o : import 단축기
import java.awt.Button;
import java.awt.Frame;


public class UIEx {

	public static void main(String[] args) {
		// 자바에서 화면 만들기
		Frame f = new Frame(); // 판때기 생성
		Button b = new Button("머튼 이름"); // 버튼 생성
		f.add(b); // 판때기에 버튼 추가

		f.setSize(300, 300); // 판때기 크기 설정
		f.setLocation(500, 300); // 판때기 위치 설정
		f.setVisible(true); // 판때기 화면에 보여주기
	}

}
