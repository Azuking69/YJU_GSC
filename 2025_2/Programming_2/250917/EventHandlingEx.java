
// 버튼 클릭 이벤트 처리
import javax.swing.JButton;
import javax.swing.JFrame;
// ctrl + shift = o : import 
class MyFrame{
	JFrame jf;
	JButton jb;
	
	public MyFrame() {
		jf = new JFrame("판때기이름");
		jb = new JButton("나는 버튼");
		
		jf.add(jb); // 판때기에 버튼 추가
		jf.setSize(300, 300); // 판때기 크기 지정
		jf.setLocation(200, 200); // 판때기 위치 지정
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // 간제증료활
		jf.setVisible(true); // 화면에 보여주겠다
	}
}

public class EventHandlingEx {
	public static void main(String[] args) {
		new MyFrame();
	}
}