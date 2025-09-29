import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class IOEx {
	public static void main(String[] args) throws IOException {
		// 1) byte stream class 사용
		// 파일에 데이터 쓰기
		
		// 1-1)
		//FileOutputStream fos 
		//= new FileOutputStream("c://javatest/text.txt");
		//fos.write('A'); // 1byte
		//fos.write('B'); // 1byte
		//fos.write(67); // 1byte (아스키코드 : "C")
		//fos.write('가'); // 파일에 쓰디 제대로 동작하지 않음 => 한글표현(유니코드)을 위해 최소 2byte　
		
		
		// 1-2)
		FileOutputStream fos 
		= new FileOutputStream("c://javatest/text.txt");
		BufferedOutputStream bos
		= new BufferedOutputStream(fos);
		
		String str = "ABC가나다";
		byte[] r = str.getBytes(); // 문바열 -> byte배열 변화
		bos.write(r);
		bos.flush(); // 버퍼에 쌓인거 밀어내기
		
		// 파일에서 데이터 읽기
		FileInputStream fis 
		= new FileInputStream("c://javatest/text.txt");
		int result = fis.read();
		System.out.println((char)result);
		result = fis.read();
		System.out.println((char)result);
		result = fis.read();
		System.out.println((char)result);
		result = fis.read();
		System.out.println((char)result);
		
		
	}
}