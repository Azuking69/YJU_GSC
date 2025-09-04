package Java_drill.drill_003;

import java.util.Scanner;

public class main3_22 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.print("정수를 입력하세요: ");
        // 입력 받기
        int num = scanner.nextInt();

        // 계산
        int mask = 1 << 1;
        int result = num ^ mask;
        // 출력
        System.out.println(result);

        // close
        scanner.close();
    }
}
