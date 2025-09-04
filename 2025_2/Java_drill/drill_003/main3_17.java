package Java_drill.drill_003;

import java.util.Scanner;

public class main3_17 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("정수를 입력하세요: ");
        // 일벽 받기
        int num = scanner.nextInt();
        
        // 계산
        int doubledNumber = num * 2;
        // 출력
        System.out.println(doubledNumber);

        // close
        scanner.close();
    }
}
