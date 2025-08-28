package Java_drill.drill_003;

import java.util.Scanner;

public class main3_2 {
    public static void main(String[] args) {
        // 입력준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("반지름을 입력해주세요: ");
        // 입력 받기
        double num = scanner.nextDouble();
        // 계산
        double total = num * num * 3.14159265;
        // 출력
        System.out.println(total); 
        // close
        scanner.close();
    }
}
