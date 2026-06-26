// 클래스의 구성 요소 예제
class ClassComponents {
    // 1 : 멤버변수(필드) - 객체의 속성 저장
    String name;
    int age;
    
    // 2 : 초기화 블록 - 생성자보다 먼저 실행됨
    {System.out.println("초기화 블록 실행!");}

    // 3 : 생성자 - 객체 생성 시 자동 호출(객채 초기화 작업)
    ClassComponents(String name, int age){
        this.name = name;
        this.age = age;
        System.out.println("생성자 실행! 객체 생성됨.");
    }

    // 4 : 멤버 메소드 - 객체의 동작 정의
    void introduce(){
        System.out.println("저는" + name + "이고, " + age + "살입니다.");
    }

    // 5 : 소멸자 (자바에서는 명확한 소멸자가 없음, GC가 자동 관리)
}
