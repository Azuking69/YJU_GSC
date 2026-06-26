
// abstract class (추상화 class) : 추상화 메소드를 1개 이상가지는 class
// 문법적으로 추상화 클래스는 클래스 선언부 앞에 "abstract" 선언에 주어야 함
// 추상화 클래스는 객체화가 블가능

// abstract method (추상화 method) : 기능이 구현되어 있지 않은 메소드
// 문법적으로 추상화 메소드에 기능이 구현되어 있지 않는 의미는 아예 기능 구현부에 해당하는 "{}" 파트가
// 존재하지 않아야 함
// 추가적으로 메소드 전늬 끝부분 ";"으로 마무리
// 최종적으로 메소드 정의 앞 부분에 "abstract" 선언

// 그럼 추상화 메소드는 도대체 언제 사용하나? 
// 기능도 없는데 어다에 쓸려고 만들어 됬나?

class MyAbs {
	abstract public void printX();
}

abstract class Animal{
	abstract public void cry();
	public void setType(){
		System.out.println("type");
	}
}

class Cat extends Animal{
	public void cry(){
		System.out.println("야옹");
	}
}

class Dog extends Animal{
	public void cry() {
		System.out.println("멍멍");
	}
}


public class AbstractEx {
	public static void main(String[] args) {
		Animal a = new Dog();
		a.cry();
		
		Animal b = new Cat();
		b.cry();
	}
}
