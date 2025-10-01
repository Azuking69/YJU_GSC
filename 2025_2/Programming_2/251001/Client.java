import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;

public class Client {
	public static void main(String[] args) throws UnknownHostException, IOException {
		// TCP/IP network 통신
		
		
		// Client 파트 종이컵 생성
		Socket client = new Socket("210.101.236.171", 8888);
		// 쓰기 위한 실 뽑아내기
		OutputStream os = client.getOutputStream();
		
		

	}
}