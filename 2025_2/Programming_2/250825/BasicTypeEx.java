
public class BasicTypeEx {

	public static void main(String[] args) {
		
		// 자바에서 변수 생성
		// 지바에서 변수를 민들때에는 해당 변수가 가질 수 있는 자료를 지정해주어야 
		
		// 자바 기본 자료형
		// (1) 정수형(byte-short-int-long)
			byte b = 10; // 1byte 용량 => 2~8 = 256, -128~127 숫자 저장
			b = -128;
//			b = -129; // 범위초과
			b = 127;
//			b = 128; // 범위초과
			
			short s = -129; // 2byte 용량
			s = 128;
			
			int i = 99999; // 4byte 용량
			
			long l = 9999999; // 8byte 용량
			
			b = 90;
//			b = b + 10; // 실술연산
			
			b = 90; // -128~127
//			b = b - 1; // 불가능 
//			short s1 = b - 1; // 불가능
			// 잦바에서 정수형 실술연산이 이뤄지게 되면 int형으로 암목적으로 간주
			// 따라서  b - 1 => int 타입이 된
			int i1 = b - 1; // 가능
			//그래서 우리는 정수형을 사용할때 맘편히 int 타입을 사용하면 된다.
			// 자바에 정수형의 암목적인 디펄트형은 int type!
			
		// (2) 실수형(float-double, default type = double)
//			float f = 0.1; // 0.1은 double 타입으로 인식된므로 오류
			float f = 0.1f; // bps, Bps 차이
			double d = 0.1;
			
		// (3) 문자형
			char c = 'A';
			System.out.println(c);
			c = 66; // ASKⅡ코드
			System.out.println(c);
			
		// (4) boolean형
			c 
			
	}

}
