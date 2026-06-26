package Java_drill.drill_003;

import java.util.Scanner;

public class main3_1 {
    public static void main(String[] args) {
        // 입력준비
        Scanner scanner = new Scanner(System.in);
        // 숫자 두 개 입력
        System.out.println("정수를 두 개 입력하세요: ");
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        // 계산
        int sum = num1 + num2;
        // 출력
        System.out.println(sum);
        // close
        scanner.close();
    }
    
}
