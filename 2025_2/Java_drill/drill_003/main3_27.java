package Java_drill.drill_003;

import java.util.Scanner;

public class main3_27 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지(정수)
        System.out.print("정수를 입력하세요: ");
        // 입력 받기
        int num1 = scanner.nextInt();
        // 입력 내용 표지(소수)
        System.out.print("소수를 입력하세요: ");
        // 입력 받기
        double num2 = scanner.nextDouble();

        // 소수를 정수로 바꾸기
        int doublenum2 = (int) num2;
        // 정수 + 소수 계산
        int result = num1 + doublenum2;
        // 출력
        System.out.println(result);

        // close
        scanner.close();
    }
}
