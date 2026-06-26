import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

public class AttClient {

	public static void main(String[] args) throws UnknownHostException, IOException {
		Socket client = new Socket("10.30.14.160", 8889);
		String str = "이케다아즈키:Y";
		client.getOutputStream().write(str.getBytes());

	}
}