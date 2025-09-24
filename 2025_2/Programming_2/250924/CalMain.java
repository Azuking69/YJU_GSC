
public class CalMain {
	public static void main(String[] args) {
//		new CalUI();
		CalLogic c = new CalLogic();
		int r = c.doIt("3+2-1");
		System.out.print(r);
	}
}