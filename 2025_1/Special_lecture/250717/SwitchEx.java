
public class SwitchEx {
	public static void main(String[] args) {
		int score = 99;
		System.out.println(score/10);
		switch (score/10) {
		case 9:
			System.out.println("A");
			break;
		case 8:
			System.out.println("B");
			break;
		case 7:
			System.out.println("C");
			break;
		default:
			System.out.println("F");
			break;
		}it
		
		if(score >= 90) {
			System.out.println("A");
		}else if (score >= 80) {
			System.out.println("B");
		}else if (score >= 70) {
			System.out.println("C");
		}else {
			System.out.println("F");
		}
		
		//switまで入力してCTRL+スペースを押すと予測出てくる
		int r = 9;
		switch (r) {
		case 1:
			System.out.println("1등");
			break;
		case 2:
			System.out.println("2등");
			break;
		case 3:
			System.out.println("3등");
			break;
		case 4:
			System.out.println("4등");
			break;
		default:
			System.out.println("탈락");
			break;
		}
	}
}