class Car{
    String brand; // 맴버변수(Heap에 저장됨)

    // 생성자: 객체가 생성될 때 브랜드를 초기화
    Car(String argBrand){
        brand = argBrand;
    }
}

public class RefVariableExam1Main {
    public static void main(String[] args) {
        // 참조 변수 선언 및 객체 생성(Heap 메모리에 저장)
        Car myCar1 = new Car("Genesis"); // "Genesis" 객체 생성 후, myCar1이 참조
        Car myCar2 = new Car("BMW"); // "BMW" 객체 생성 후, myCar2이 참조
        Car myCar3 = new Car("Tesla"); // "Tesla" 객체 생성 후, myCar3이 참조
    
        // 참조 변수 복사 (myCar4는 myCar2와 같은 객체를 가리킴)
        // myCar2와 myCar4는 같은 객체를 가리키므로,
        // myCar2가 변경되면 myCar4도 동일한 영향을 받음
        Car myCar4 = myCar2;
    }
}