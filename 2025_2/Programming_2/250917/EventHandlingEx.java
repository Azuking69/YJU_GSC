

// ctrl + shift = o : import 단측키
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextField;


class MyListener2 implements ActionListener{
	@Override
	public void actionPerformed(ActionEvent e) {
		//버튼 클릭 or 엔터키 입력시 호출되는 콜백메소드
		System.out.println("엔터키 입력");
	}
}

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
	JTextField jf; //한줄 입력창
	
	public MyFrame() {
		// jf = new JFrame("판때기 이름");
		super("판때기 이름"); // 상위클래스 생성자 호출 -> new JFrame("판때기 이름")
		jb = new JButton("나는 버튼");
		jf = new JTextField(15); // 15칸 한줄 입력창
		
		// 화면 배치 관리자
		// 다망한 해성도를 가지는 디바이스에서 화면에 보여지게 되면
		// 절대좌표값으로 설정된 화면은 해상도마다 다르게 보일 수 있게됨
		// 따라서 다양한 해상도에서 일관된 화면을 보여주기 위해
		// UI 구성시 절대좌표값을 사용하지 않고
		// 대신 화면 배치관리자를 사용함		
		
		// FlowLayout : 가장 기본적인 화면배치 관리자
		// 화면에 들어오는 순서대로 최소한의 크기로 배치
		FlowLayout layout = new FlowLayout();
		
		// 판때기에 화면 배치관리자 설정
		this.setLayout(layout);
		
		
		// 버튼 클릭 감시자 객체화
		MyListner m = new MyListner();		
		jb.addActionListener(m); // 버튼 감시자 달아주기
		
		MyListener2 m2 = new MyListener2();
		jf.addActionListener(m2);
		
		add(jf); // 판때기에 입력창 추가
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