package Java_drill.drill_003;

import java.util.Scanner;

public class main3_25 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지(정수)
        System.out.print("정수를 입력하세요: ");
        // 입력 받기
        int num = scanner.nextInt();
        // 입력 내용 표지(시프트하는 정수)
        System.out.print("시프트하는 수를 입력하세요: ");
        // 입력 받기
        int shift = scanner.nextInt();

        // 계산
        int result = num << shift;
        // 출력
        System.out.println(result);

        // close
        scanner.close();
    }
}
