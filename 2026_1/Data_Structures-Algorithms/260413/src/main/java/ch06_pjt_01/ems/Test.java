package ch06_pjt_01.ems;

import java.util.HashMap;
import java.util.Map;

class User {
	public String firdtName;
    public User(String firdtName) {
        this.firdtName = firdtName;
    }

}


public class Test {
    public static  void main(String[] args) {
        Map map = new HashMap();
        User user = new User("SHIN");

        map.put(user, "0000");
        System.out.println(map.get(user));

        map.put("ABC", "1111");
        System.out.println(map.get("ABC"));

        map.put(new User("SHIN"), "0000");
        System.out.println(map.get(new User("SHIN")));

//        map.put("ABC", "1111");
//       map.put("ABC", "3333"); //UPDATE
//        map.put("DEF", "2222");
//        map.put("GHI", "3333");
//        map.put("JKL", "4444");
//        map.put("MNO", "5555");
//        map.put("PQR", "6666");


    }
}
