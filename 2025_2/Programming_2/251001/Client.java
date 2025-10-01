import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;

import javax.swing.JFrame;
import javax.swing.JTextField;

class ClientUI extends JFrame{
	JTextField jf;
	
	// Inner class(내부 클래스)
	class MyUIListener implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			// callback method
			
			// TCP/IP network 통신		
			// Client 파트 종이컵 생성
			try {
				Socket client = new Socket("210.101.236.171", 8888);
				// 쓰기 위한 실 뽑아내기
				OutputStream os = client.getOutputStream();
				String msg = jf.getText(); // 입력창에 입력된 문자열 가져오기
				os.write(msg.getBytes("utf-8"));
				jf.setText(""); // 입력창 초기화
			}catch(Exception ignore) {
				System.out.println("문제발생");
			}
		}
	}
	
	public ClientUI() {
		jf = new JTextField(15);
		this.add(jf); // 판때기에 ㅇ비력창 추가
		setSize(300, 100);
		setLocation(200, 200);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setVisible(true);
	}
}

public class Client {
	public static void main(String[] args) throws UnknownHostException, IOException {
//		// TCP/IP network 통신		
//		// Client 파트 종이컵 생성
//		Socket client = new Socket("210.101.236.171", 8888);
//		// 쓰기 위한 실 뽑아내기
//		OutputStream os = client.getOutputStream();
//		String msg = "안녕";
//		os.write(msg.getBytes("utf-8"));

	}
}