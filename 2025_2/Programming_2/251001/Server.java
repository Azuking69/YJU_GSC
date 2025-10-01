import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
	public static void main(String[] args) throws IOException {
		// TCP/IP 기반의 network 통신
		
		// 서버 파트 종이컵 만들기
		ServerSocket ss = new ServerSocket(8888);
		while(true) {
			Socket server = ss.accept(); // 클라이언트 접속대기 + 종이컵 생성
			
			// 읽기 위한 실 거저오기
			InputStream is = server.getInputStream();
//			InputStream is2 = new InputStream(); 객체화 불가능
			byte b[] = new byte[1024];
			is.read(b);
			String str = new String(b);
			System.out.println("end");
		}
	}
}