class Parent{
    void show(){
        System.out.println("Parent 클래스의 메소드");
    }
}

// Child 클래스는 Parent 클래스를 상속하여 선언됨
// Child 클래스는 Parent 클래스를 상속받은 자식 클래스이다
class Child extends Parent{
    void show(){
        System.out.println("Child 클래스의 메소드(오바라이딩)");
    }
}

public class Main {
    public static void main(String[] args) {
        Parent obj = new Child(); // 부모 타입 참조 변수로 자식 객체 참조
        obj.show(); // Child 클래스의 메소드 실행 (다형성) 
    }
}