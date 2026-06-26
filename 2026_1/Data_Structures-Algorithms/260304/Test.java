// 인터페이스는 상수, 추상화메소드만 구성됨
interface MyInter{
    abstract public void add();
}

class A implements MyInter{
    @Override
        public void add(){

        }
}

class B extends A{

}


public class Test {
    public static void main(String[] arg){
        MyInter m1 = new A();
        MyInter m2 = new B();
        // MyInter mt = new MyInter(); => error



        A a = new A();
        B b = new B();
        A c = new B();
        // B d = new A(); => error
    }
}
