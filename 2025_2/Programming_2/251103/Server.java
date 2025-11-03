
// 서버파트 구현 목록
// 1) 클라이언트 접속 대기 → 접속 후 클라이언트와 매칭되는 종이컵(Socket) 생성
// 2) 접속한 모든 클라이언트로 부터 메시지 수신 → 수신된 메시지를 모든 클라이언트로 송신
// : 클라이언트 수 + 1 개의 Thread 필요

import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
	public static void main(String[] args) throws IOException {
		// 1) 클라이언트 접속 대기
		ServerSocket ss = new ServerSocket(8888);
		while (true) { // 여러 클라이언트 접속을 받아주기 위해 반복문 사용
		// 클라이언트 접속대기 + 접속하면 종이컵 만들어주기
			Socket server = ss.accept(); 
			
			// 2) 접속한 모든 클라이언트로 부터 메시지 수신
			InputStream is = server.getInputStream(); // 종이컵에서 읽기 위한 실 뽑아내기
		}
		
		
		
		
	}

}
