// Client 파트 구현 목록
// 1) 서버에 접속(Socket 생성) - 접속 버튼 클릭되었을 때
// 2) 서버로 메시지 승신
// 3) 서버에서 보내는 메시지 수신

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.io.InputStream;
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



//채팅 메시지 입력창, 대화창이 기본적으로 제공되는 클라이언트 화면구현
class ClientUI extends JFrame {
	JButton con;   // 서버 접속을 위한 버튼
	JTextField jtf; // 채팅 메시지 입력창
	JTextArea jta; // 지난 채팅 메시지를 볼 수 있는 대화창
	
	Socket client; //서버외의 통신 위한 종이컵
	OutputStream os; // 서버에 데이터를 전송하기 위한 실
	InputStream is; // 서버에 데이터를 수진하기 위한 실
	
	// 서버에 접속을 성공하고 나면 Thread
	class ClientThread extends Thread{
		public void run() {
			//3) 서버에서 보내는 메시지 수신
			while(true){
				try {
				// 종이컵에서 읽기 위한 실 뽑아내기
				
				byte[] b = new byte[1024];
				is.read(b); // 1024byte 읽어서 배열 b에 저장
				// 수진된 메시지 화면에 보여주기
				String str = new String(b); // 바이트값 -> 문자열 변환
				jta.append(str.trim() + "\n"); // 빈공백 제거 후 화면에 보여주기
				
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
			
		}
	}
	
	class MyListner implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			// callback method
			// 버튼이 클릭되거나 "enter"키가 입력되면 호출되는 콜백 메소드
			
			// 버튼이 늘려졌는지 "enter"키가 눌려졌는지 구분
			// 늘리진 버튼에 이름 가져오기
			String str = e.getActionCommand();
			if(str.equals("접속")) {
				try {
					// 1) 서버에 접속(Socket 생성)
					client = new Socket("127.0.0.1", 8888);
					// 서버 접속을 성공하고 나면
					is = client.getInputStream();
					os =client.getOutputStream();
					new ClientThread().start(); // 成功したときのみ
				} catch (IOException e1) {
					e1.printStackTrace();
				}
				System.out.println("서버접속 버튼 클릭됨");
				
			}else { // 입력창에 "enter"key 입력되었을 때
				// 2) 서버로 메시지 승신
				String msg = jtf.getText(); // 입력창에서 문자열 가져오기
				try {
					os.write(msg.getBytes());
				} catch (IOException e1) {
					e1.printStackTrace();
				}
			}
		}
	}

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



