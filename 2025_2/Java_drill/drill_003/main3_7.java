package Java_drill.drill_003;

import java.util.Scanner;

public class main3_7 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("나이를 입력하세요: ");
        // 입력 받기
        int age = scanner.nextInt();
        
        // 나이 판단
        if (18 < age){
            System.out.println("성인");
        }else{
            System.out.println("미성년");
        }

        // close
        scanner.close();
    }
}
