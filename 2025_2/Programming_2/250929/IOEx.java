import java.io.FileOutputStream;
import java.io.IOException;

public class IOEx {
	public static void main(String[] args) throws IOException {
		// 1) byte stream class 사용
		// 파일에 데이터 쓰기
		
		//FileOutputStream fos 
		//= new FileOutputStream("c://javatest/text.txt");
		//fos.write('A'); // 1byte
		//fos.write('B'); // 1byte
		//fos.write(67); // 1byte (아스키코드 : "C")
		//fos.write('가'); // 파일에 쓰디 제대로 동작하지 않음 => 한글표현을 위해 최소 2byte　
		                  // 2byte (유니코드) -> 표지할 수 없음
		
		
		FileOutputStream fos 
		= new FileOutputStream("c://javatest/text.txt");
				String str = "가나다";
		byte[] r = str.getBytes(); // 문바열 -> byte배열 변화
		fos.write(r);
		
		
		
	}
}