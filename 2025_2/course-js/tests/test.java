package oopVer.MethodChangeng;

class Bar{
  int x = 1;
}

class Foo extends Bar{
  int x = 2;
  Foo(){
    super();
  }
}

// 실행 클래스
public class TestMain{
  public static void main(String[] args){
    Bar b = new Foo();
    System.out.println(b, x)
  }
}