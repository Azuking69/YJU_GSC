package programming_1.Special_lecture.250709;

public 

public class StringEx {

	public static void main(String[] args) {
		// String class의 두 가지 특징
		// 1) 암묵적인 객체 생성을 지원
		String str = new String("ABC");
		String str2 = "ABC";
		
		// 문자열 값 비교를 할 경우에는 "==" 사용금지!
		// str, str2에는 주소값이 들어가 있으므로 "ABC"문자열에 값 비교를 하는게 아니라 주소값 비교를 하게됨
		// if(str == str2){ // 문자열 값비교를 위해 잘못된 코드
		if(str == str2) { // str과 str2 객체의 문자열 값비교
			System.out.println("같다");
		}else {
			System.out.println("다르다");
		}
		
		String str3 = "ABC";
		String str4 = "ABC";
		
		if(str3 == str4) {
			System.out.println("같다");
		}else {
			System.out.println("다르다");
		}
		
		
		// 2) 불변적인 특징 : 문자열 값 변경 불가능
		String msg = "ABC";
		msg = msg + "D";
		msg = msg + "E";
		
		// 한번 만들어진 String 객체는 변경이 불가능 하므로 위와 같이 문자열 변경 작업이 일어나면 
		// 실제 메모리에는 "ABC", "ABCD", "ABCDE" 새개의 객체가 존재하게 됨
		// 각각 변경시마다 해당 문자열값을 가지는 객체 주소가 msg 변수에 할당됨
		
		// 그렇다면 미친듯이 문자열 수정을 하게되면 문자열 객체가 미친듯이 만들어진다.
		// 하지만 메모리는 유한하고 지속적으로 사용되지 않는 문자열 객체가 메모리를 쓸 때 없이 차지하게 되는
		//상황을 우리는 메모리 누수!라고 이야기 한다 
		
		// 이런 상황을 방지하려면 메모리에 더 이상 사용되지 않는 자원들에 대한 필요
		// 하지만 Java는 객체 할당(new)는 문법적으로 지원하나 객체 해새 분법은 지원하지 않는다!
		// 객체 해제 문법이 지원되지는 않지만 대신 Java에서 GC(Gabage Collector)가 사용되지 않는
		// 객체를 해제 해 준다
	}

}
 StringEx {
    
}
