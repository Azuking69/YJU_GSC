// Client 파트 구현 목록
// 1) 서버에 접속(Socket 생성)
// 2) 서버로 메시지 승신
// 3) 서버에서 보내는 메시지 수신

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.io.OutputStream;
import java.lang.foreign.AddressLayout;
import java.net.Socket;
import java.net.UnknownHostException;
import java.time.chrono.IsoChronology;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTabbedPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;


// 클라이언트 화면에서 처리되어야 하는 이벤트 목록
// -> "접속" 버튼을 클릭시 서버애 접속
// -> 대화창에 "enter" 입력시 서버로 메시지 전송
class MyListner implements ActionListener{
	@Override
	public void actionPerformed(ActionEvent e) {
		// callback method
		// 버튼이 클릭되거나 "enter"키가 입력되면 호출되는 콜백 메소드
		
		// 버튼이 늘려졌는지 "enter"키가 눌려졌는지 구분
		// 늘리진 버튼에 이름 가져오기
		String str = e.getActionCommand();
		if(str.equals("접속")) {
			System.out.println("서버접속 버튼 클릭됨");
		}else {
			jta.settext("Enter");
			System.out.println("Enter 늘리짐");
		}
	}
}

//채팅 메시지 입력창, 대화창이 기본적으로 제공되는 클라이언트 화면구현
class ClientUI extends JFrame {
	JButton con;   // 서버 접속을 위한 버튼
	JTextField jtf; // 채팅 메시지 입력창
	JTextArea jta; // 지난 채팅 메시지를 볼 수 있는 대화창

	public ClientUI() {
		super("이것은 클라이언트");
		con = new JButton("접속");
		jtf = new JTextField(20);
		jta = new JTextArea(30, 30);
		
		// 접속버튼 event handling
		// 감시자 객체화
		MyListner m = new MyListner();
		// 접속 버튼에 감시자 달아추기
		con.addActionListener(m);
		
		// 입력창 event handling
		// 한줄 입력창에 감시자 달아추기
		jtf.addActionListener(m);
		
		
		FlowLayout layout = new FlowLayout(); // 화면 배치 관리자
		setLayout(layout); // 현재 판대기에 배치 관리자 설정
		add(jtf); // 판대기에 한줄 입력창 먼저 배치
		add(con); // 그다음 접속버튼
		add(jta); // 마지막으로 대화창 배치
		
		jta.setText("가나다라");
		jta.setText("마바사");
		jta.append("abc");
		jta.append("def");
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // 강제종료 기능 활성화
		setSize(300, 500); // 판대기 사이즈 조절
		setLocation(250, 250); // 판대기 보여질 위치 조절
		setVisible(true); // 판대기 화면에 보여주기
		
	}
}

public class Client {
	public static void main(String[] args) throws UnknownHostException, IOException {
		new ClientUI();
		// 1) 서버에 접속(Socket 생성)
//		Socket client = new Socket("127.0.0.1", 8888);
		
		// 2) 서버로 메시지 승신
//		OutputStream os = client.getOutputStream();
//		os.write("카츠동");
	}
}



