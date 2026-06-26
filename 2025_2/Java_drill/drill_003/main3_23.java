package Java_drill.drill_003;

import java.util.Scanner;

public class main3_23 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.print("정수를 두 개 입력하세요: ");
        // 입력 받기
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        
        // bit 계산
        int result = num1 & num2;
        // 출력
        System.out.println(result); 

        // close
        scanner.close();
    }
}
