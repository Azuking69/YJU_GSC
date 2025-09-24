
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
		
		
		// (2)불변적인 특징
		String temp = "ABC";
		temp = temp + "D"; //"ABC", "ABCD"
		// 문자열 수정이 빈번하게 일어나면 수정된 객체가 계속 생성
		// 쓸때없이 메모리 공간을 차지하게 됨
		// 결국 메모리 누수 문제를 야기하게 됨
		// 문자열 수정이 빈번하게 일어나는 경우라면
		// String class 대신 StringBuffer class등을 사용해야 함

	}

}
