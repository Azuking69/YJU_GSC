// Client 파트 구현 목록
// 1) 서버에 접속(Socket 생성)
// 2) 서버로 메시지 승신
// 3) 서버에서 보내는 메시지 수신

import java.net.Socket;

public class Client {
	public static void main(String[] args) {
		// 1) 서버에 접속(Socket 생성)

		Socket client = new Socket("127.0.0.1", 8888);

	}
}