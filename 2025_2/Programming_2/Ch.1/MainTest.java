
// 클래스 선언
class Car{
    String brand; // 멤버 변수
    
    Car(String brand){ // 생성자
        this.brand = brand;
    }

    void drive(){ // 메소드
        System.out.println(brand + "자동차가 주행 중입니다.");
    }
}

// 실행 코드
public class MainTest {
    public static void main(String[] args) {
        // 객체 생성
        Car car1 = new Car("Hyundai"); // 참조 변수 car1이 Car 객체를 가리킴
        Car car2 = new Car("BMW"); // 참조 변수 car2가 Car 객체를 가리킴

        // 객체의 멤버 사용(참조 변수 + "," 연산자)
        System.out.println(car1.brand); // Hyundai
        car1.drive(); // Hyundai 자동차가 주행 중입니다

        System.out.println(car2.brand); // BMW
        car2.drive(); // BMW 자동차가 주행 중입니다.
    }
}
