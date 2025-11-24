

class Camera{
	static Camera c; // 3) static 있으면 아래에서도 사용할 수 있음
	private Camera() {
		
	}
	
	public static Camera open() { // 2) static 없으면 될 수 있음
		c = new Camera(); // 1) Private Camera(); 때문에
		플래시온(); // 4) 아래에 static 있으면 호출 됨
		return c;
		
//		return new Camera();
	}
	
	public static void 플래시온() {
//		
//	}
//	
//	public void 플래시오프() {
//		
//	}
}


public class SingltonEx {
	public static void main(String[] args) {
		Camera c1 = Camera.open();
//		Camera c1 = new Camera(); // Camera class 안을 다 가져오기
//		c1.플래시온();
		
		Camera c2 = new Camera();
//		c2.플래시오프();

		
	}

}
