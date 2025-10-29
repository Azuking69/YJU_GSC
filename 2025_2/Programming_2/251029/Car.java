import java.util.List;
import java.util.ArrayList;

public class Car {
	public List<String> carList = null;
	public Car() {
		carList = new ArrayList<String>();
	}
	public String getCar() {
		String carName = null;
		switch ((int) (Math.random() * 3)) {
		case 0 :
			carName = "SM5";
			break;
		case 1 :
			carName = "매그너스";
			break;
		case 2 :
			carName = "카렌스";
			break;
		}
		return carName;
	}
	
	public synchronized String pop(){
		String carName = null;
		if (carList.size() == 0) {
			try {
				System.out.println("차가 없어요. 생산할 때까지" + "기다리세요.");
				this.wait();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		carName = (String) carList.remove(carList.size() - 1);
		System.out.println("손님이 차를 사겠습니다." + "손님이 구입한 차 이름은=>₩" + carName + "₩");
		return carName;
	}
}