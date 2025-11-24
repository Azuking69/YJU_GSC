import java.awt.desktop.OpenFilesEvent;

class Camera{
	public static Camera open() {
		return new Camera();
	}
	
	public void 플래시온() {
		
	}
	
	public void 플래시오프() {
		
	}
}


public class SingltonEx {
	public static void main(String[] args) {
		Camera c1 = Camera.open();
//		Camera c1 = new Camera(); // Camera class 안을 다 가져오기
		c1.플래시온();
		
		Camera c2 = new Camera();
		c2.플래시오프();

		
	}

}
