package Java_drill.drill_003;

import java.util.Scanner;

public class main3_14 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("정수 두 개를 입력하세요: ");
        // 입력 받기
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();

        // 입력된 정수가 플러스인지 마이너스인지 판단
        if (num1 < 0 && num2 < 0){
            System.out.println("양쪽이 양의 정수가 아닌니다.");
        } else {
            System.out.println("적어도 하나는 양의 정수입니다.");
        }

        // close
        scanner.close();
    }
}
