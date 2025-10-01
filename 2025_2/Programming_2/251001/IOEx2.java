import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class IOEx2 {

	public static void main(String[] args) throws IOException {
		// character stream 계열을 사용하여 파일에 읽고/쓰기
		FileWriter fw = new FileWriter("c://javatest/text.txt");
		fw.write("가나다ABC"); //
		fw.flush(); // 중요!
		
		FileReader fr = new FileReader("c://javatest/text.txt");
		BufferedReader br = new BufferedReader(fr);
		String result = br.readLine(); // 한 줄 읽기		
//		int result = fr.read();
//		System.out.println((char)result);
		System.out.println(result);
	}
}