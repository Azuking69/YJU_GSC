// ctrl + shift + o : import 단축기
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextField;
import java.awt.FlowLayout;


// ctrl + shift + f : 들여쓰기 자동조정
// 계산기 화면
class MyUI extends JFrame{ // has a 관계 : My class가 JFrame (판때기)를 가지고 
	// 자바에서 화면 만들기
	JFrame f ; 
	JTextField tf; // 한줄 입력장
	JButton[] button;
	JButton b0;
	JButton b1;
	JButton b2;

	
	public MyUI() {
		button = new JButton[10];
		for(int i = 0; i < 10; i++) {
			button[i] = new JButton(""+i);
			f.add(button[i]);
		}
		
		f = new JFrame(); // 판때기(板) 생성
		tf = new JTextField(20);
		b0 = new JButton("0"); // 버튼 생성
		b1 = new JButton("1");
		b2 = new JButton("2");
		
		// 화면 배치 관리자
		// FlowLayout : 배치되는 순서대로 최소한의 크기로 화면에 UI
		FlowLayout layout = new FlowLayout();
		f.setLayout(layout); // 배치관리자 설정
		// f.setFlowLayout(null); // 배치관리자 초기화
		
		f.setLayout(null); // 배치관리자(バッチ管理者) 초기화
		b0.setSize(50, 50);
		b0.setLocation(0, 0);
		b1.setSize(50, 50);
		b1.setLocation(50, 0);
		b2.setSize(50, 50);
		b2.setLocation(100, 0);
		
		f.add(tf); // 판때기에 호출 입력창 추가
		f.add(b0); // 판때기에 버튼 추가	
		f.add(b1);
		f.add(b2);
		
		// 강제종료 활성화
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setSize(300, 300); // 판때기 크기 설정
		f.setLocation(500, 300); // 판때기 위치 설정
		f.setVisible(true); // 판때기 화면에 보여주기
	}
}


// is a 관계 : MyUI2 class가 JFrame(판때기)를 상속 받고 있다
class MyUI2 extends JFrame{
	JButton b0, b1, b2;
	public MyUI2() {
		b0 = new JButton("0");
		b1 = new JButton("1");
		b2 = new JButton("2");
		
		this.add(b0); // 현제 큰내스내의 add() 메소드 호출
		add(b1); // this. 생략이 가능
		add(b2);
	}
}


public class UIEx {
	public static void main(String[] args) {
		new MyUI();
	}
}
