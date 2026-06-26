package Java_drill.drill_003;

import java.util.Scanner;

public class main3_28 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.print("정수를 입력하세요: ");
        // 입력 받기
        double num = scanner.nextDouble();

        // 소수를 정수로 바꾸기
        int intnum = (int) num;
        // 출력
        System.out.println(intnum);

        // close
        scanner.close();
    }
}
