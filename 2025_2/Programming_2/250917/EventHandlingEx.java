


import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
// ctrl + shift = o : import 단측키

// 버튼 클릭 감시자 정의
class MyListner implements ActionListener{
	@Override
	public void actionPerformed(ActionEvent e) {
		// callback method
		// 프로그래머가 호출하는 메소드가 아님
		// 시스템이 호출해주는 메소드임
		// 근데 코딩은 내가 해줌
		// 그럼 이 메소드가 어떤 조건에서 호출되는지 알아야
		// 내가 무슨 코딩을 해줘야 될지 알수 있다
		// 따라서 콜백메소드라는 얘기를 들으면??
		// 어떤 상황(조건)에서 그 메소드가 호출되는지 조건 부터 파악!
		
		
		// 버튼이 클릭되었을때 호출되는 메소드
		System.out.println("버튼 클릭 됨");
	}
	
}

// 버튼 클릭 이벤트 처리
class MyFrame extends JFrame{
	// JFrame jf;
	JButton jb;
	
	public MyFrame() {
		// jf = new JFrame("판때기 이름");
		super("판때기 이름"); // 상위클래스 생성자 호출 -> new JFrame("판때기 이름")
		jb = new JButton("나는 버튼");
		
		// 버튼 클릭 감시자 객체화
		MyListner m = new MyListner();
		
		jb.addActionListener(m); // 버튼 감시자 달아주기
		
		this.add(jb); // 판때기에 버튼 추가
		this.setSize(300, 300); // 판때기 크기 지정
		this.setLocation(200, 200); // 판때기 위치 지정
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // 간제증료활
		this.setVisible(true); // 화면에 보여주겠다
	}
}

public class EventHandlingEx {
	public static void main(String[] args) {
		new MyFrame();
	}
}