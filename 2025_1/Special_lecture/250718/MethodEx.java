
class MyMethod extends Object{
	int y = 10;
	public void printX() {
		System.out.println("X");
	}
	public void add(){
		MyX x = new MyX();
		int result = x.x + y;
		System.out.println(result);
	}
}


class MyX{
	int x = 20;
}


public class MethodEx {
	public static void main(String[] args) {
		MyMethod m = new MyMethod();
		m.printX();
		MyMethod n = new MyMethod();
		n.add();
	}
}