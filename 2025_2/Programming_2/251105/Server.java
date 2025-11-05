// 서버파트 구현 목록
// 1) 클라이언트 접속 대기 → 접속 후 클라이언트와 매칭되는 종이컵(Socket) 생성
// 2) 접속한 모든 클라이언트로 부터 메시지 수신 → 수신된 메시지를 모든 클라이언트로 송신
// : 클라이언트 수 + 1 개의 Thread 필요

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.invoke.StringConcatFactory;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;


// 서버가 클라이언트 접속 대기도 하면서 클라이언트들!이 보내는 메시지 수신도 하기위해
// 두 가지 작업을 동시에 처리해 줄 수 있도록 thread를 만든다.
class ServerThread extends Thread{
	Socket server;
	
	public ServerThread(Socket server) {
	this.server = server;
	}
	
	public void run() {
		// 2) 접속한 모든 클라이언트로 부터 메시지 수신
		try {
			// 종이컵에서 읽기 위한 실 뽑아 내기
			InputStream is = server.getInputStream(); // 종이컵에서 읽기 위한 실 뽑아 내기
			byte[] b = new byte[1024];
			is.read(b); // 1024바이트 읽어서 배열 b에 저장
			// 수신된 메시지를 모든 클라이언트로 송신
			// 종이컵 저장 공간에서 종이컵을 하나씩 가져와서 해당 클라이언트로 메시지 전송
			// 그렇다는 애기는 어딘가에 여태껏 만들어진 종이컵이 다 저장되어 있는곳이 있어야 한다.
						
			
			for (int i = 0; i < Server.totalSocket.size(); i++) {
//				OutputStream os = Server.totalSocket.get(i).getOutputStream();
//				os.write(b); // 방금전에 1024바이트 만큼 읽은 데이터를 전송
				Socket temp = (Socket)Server.totalSocket.get(i);
				OutputStream os = temp.getOutputStream();
				os.write(b);
			}

		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}

class 세우버거 extends Object{
	
}


public class Server {
	static ArrayList totalSocket = new ArrayList();
	public static void main(String[] args) throws IOException {
		// 1) 클라이언트 접속 대기
		ServerSocket ss = new ServerSocket(8888);
		while (true) { // 여러 클라이언트 접속을 받아주기 위해 반복문 사용
		// 클라이언트 접속대기 + 접속하면 종이컵 만들어 주기
			Socket server = ss.accept();
			// 종이컵 저장
			totalSocket.add(server); Object s = new Socket();
			//totalSocket.add("세우튀김"); Object s = new String("세우튀김");
			//totalSocket.add(new 세우버거()); Object s = new 세우버거();
			
		}
		
				
	}
}
