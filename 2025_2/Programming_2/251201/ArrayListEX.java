import java.util.ArrayList;

class Animal{
	
}

public class ArrayListEX {
	public static void main(String[] args) {
		ArrayList a = new ArrayList();
		a.add("ABC"); // 0번째
		a.add(new Person()); // 1번째
		a.add(new Animal()); // 2번째
		
		String r1 = (String)a.get(0);
		Person r2 = (Person)a.get(1);
//		Animal r3 = (Animal)a.get(2);
		Person r3 = (Person)a.get(2);
		
		ArrayList 도형모음 = new ArrayList();
		도형모음.add(new 네모());
		도형모음.add(new 오각형());
		도형모음.add(new 삼각형());
//		도형모음.add(new Animal());
		
		// 아래 코드는 OOP가 아니다.
//		네모 x0 = (네모)도형모음.get(0); // 리턴된 값을 Object 타입 타입개스팅을 통
//		오각형 x1 = (오각형)도형모음.get(1);
//		삼각형 x2 = (삼각형)도형모음.get(2);
		
//		도형 x0 = (도형)도형모음.get(0);
//		도형 x1 = (도형)도형모음.get(0);
//		도형 x2 = (도형)도형모음.get(0);
		
		// 위에 코드 중북되는 제거해서 다음단계로 진화된 코드
		for (int i = 0; i < 도형모음.size(); i++) {
			도형 x = (도형)도형모음.get(i);
			x.그리기();
		}
		
		// 제네릭 문법 사용해서 무결성이 보장되는 자원관리
		ArrayList<도형> a = new ArrayList<도형>();
		도형모음2.add(new 네모());
		도형모음2.add(new 오각형());
		도형모음2.add(new 삼각형());
		
		도형모음2.get(0);
		
		도형 y0 = 도형모음2.get(0);
		도형 y1 = 도형모음2.get(0);
		도형 y2 = 도형모음2.get(0);
		
		for (Object x : 도형모음) {
			System.out.println(x.toString());
		}
		
//		x0.그리기();
//		x1.그리기();
//		x2.그리기();
	}

}
