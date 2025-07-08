
class MyPerson {
	int age; // member variable
	String name;
	
    // 생성자
    public MyPerson(){
    	age = 20;
    	name = "김길동";
        //System.out.println("생성자 호출");
    }
    
    public MyPerson(String n) {
    	age = 20;
    	name = n;
    }
    
    public MyPerson(int a, String n) {
    	age = a;
    	name = n;
    }
    
    public MyPerson(String n, int a) {
    	age = a;
    	name = n;
    }
}

public class ConstructorEx {
    public static void main(String[] args) {
        MyPerson p = new MyPerson();
        System.out.println(p.age);
        System.out.println(p.name);
        
       
        MyPerson p2 = new MyPerson(30, "박길동");
        System.out.println(p2.age);
        System.out.println(p2.name);
    }
    
}
