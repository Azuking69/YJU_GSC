// 자동차 클래스 
class Car{
    // 필드(멤버변수): 객체의 속성
    // 클래스 내부에 선언된 변수로, 객체의 속성을 저장
    String brand;
    int speed;

    // 생성자: 객체가 만들어질 때 실행되는 초기화 코드
    // 클래스의 객체가 생성될 때 한 번만 실행되며, 객체의 초기화 알고리즘을 수행
    Car(String brand, int speed){
        this.brand = brand;
        this.speed = speed;
    }

    // 메소드(멤버함수): 객체의 행동
    // 클래스 내부에 선언된 함수(메서드)로, 객체의 동작을 수행
    void accelerate(){
        speed += 10;
        System.out.println(brand + "속도 증가: " + speed + "km/h");
    }
    void brake(){
        speed -= 10;
        System.out.println(brand + "속도 감소: " + speed + "km/h");
    }
}

public class ObjectInstantiation {
    public static void main(String[] args) {
        // 객체 생성(실계도로 자동차를 만드는 과정)
        // 1)new Car("Hyundai", 0) → Car 클래스의 객체를 생성
        // 2)생성자가 호출되면서 Hyundai와 0이 객체의 속성으로 저장됨
        // 3)생성된 객체를 참조 변수 car1, car2에 저장
        Car car1 = new Car("Hyundai", 0);
        Car car2 = new Car("BMW", 20);

        // 객체의 메소드 호출 (자동차 운전)
        car1.accelerate(); // Hyundai 속도 증가: 10km/h
        car2.brake(); // BMW 속도 감소: 10km/h
    }
}
