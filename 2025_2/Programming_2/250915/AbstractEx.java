
class Cat{
	public void cry() {
		System.out.println("야옹");
	}
}

class Dog{
	public void cry() {
		System.out.println("멍멍");
	}
}

public class AbstractEx {
	public static void main(String[] args) {
		Cat c = new Cat();
        c.cry();

	}
}