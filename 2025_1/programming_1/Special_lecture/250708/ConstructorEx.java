
class MyPerson extends Object {
	public int age; // member variable
//	public String name; // oop관점에서 잘못된 코드
	private String name; //oop 코드
	
	
    // 생성자
    public MyPerson(){
    	this("김길동", 20);
//    	age = 20;
//    	name = ;
//      System.out.println("생성자 호출");
    }
    
    public MyPerson(String n) {
    	this(n, 20);
    }
    
    public MyPerson(int a, String n) {
    	this(n, a);
    }
    
    public MyPerson(String n, int a) {
    	age = a;
    	name = n;
    }
    
    public void setName(String n) {
    	name = n + "님";
    }
    
    public String getName() {
    	return name;
    }
}

public class ConstructorEx {
    public static void main(String[] args) {
//        MyPerson p = new MyPerson();
//        System.out.println(p.age);
//        System.out.println(p.name);
//        
//       
//        MyPerson p2 = new MyPerson(30, "박길동");
//        System.out.println(p2.age);
//        System.out.println(p2.name);
    	  
//    	  // oop관점에서 잘못된 코드
//    	  MyPerson p = new MyPerson();
//    	  p.setName("김길동" + "님"); 
//    	  p.age = 20;
//    	  
//    	  MyPerson p2 = new MyPerson(30, "박길동");
//    	  p2.setName = "박길동" + "님"; 
//    	  p2.age = 30;
//    	  
//    	  MyPerson p3 = new MyPerson();
//    	  p3.setName = "구길동" + "님"; 
//    	  p3.age = 35;
    	  
    	
    	  MyPerson p = new MyPerson();
    	  p.setName("김길동"); // oop 코드
    	  p.age = 20; // oop관점에서 잘못된 코드
    	  System.out.println(p.getName());
    	  
    	  MyPerson p2 = new MyPerson(30, "박길동");
    	  p2.setName("박길동"); 
    	  p2.age = 30;
    	  
    	  MyPerson p3 = new MyPerson();
    	  p3.setName("구길동"); 
    	  p3.age = 35;
    }
    
}
