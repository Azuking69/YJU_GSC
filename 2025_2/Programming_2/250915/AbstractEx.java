
abstract class Animal{
	abstract public void cry() {
		System.out.println("동물이 울기전에 띠링 소리");
	}
}

class Cat extends Animal{
	public void cry() { // 상속받은 메소드 기능재정의 -> 메소드 오바라이딩
		System.out.println("아옹");
	}
}

abstract class Dog extends Animal{
	public void cry() { // 상속받은 추상화 메소드 오바라이딩해서 일반
		System.out.println("멍멍");
	}
}

class Pig{
	public void cry() {
		System.out.println("꼴꼴");

	}
}

public static class AbstractEx {
	public static void main(String[] args) {
		Cat c = new Cat();
		c.cry();
		Dog d = new Dog();
		d.cry();
	}
}