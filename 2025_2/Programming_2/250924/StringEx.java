
public class StringEx {
	public static void main(String[] args) {
		
		// String class의 두가지 특징
		// (1)암목적인 객체 생성을 지원
		String str1 = "ABC"; 
		String str2 = "ABC"; 
		
		//String str1 = new String("ABC");
		//String str2 = new String("ABC");
		
		//if(str1 == str2) { // 틀린 코드!
		if(str1.equals(str2)) { // 문자열 값 비교를 위해서는 equals() 메소드 써야됨
			System.out.println("같다");
		}else {
			System.out.println("다르다");
		}

	}

}