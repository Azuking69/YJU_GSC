package Java_drill.drill_003;

import java.util.Scanner;

public class main3_19 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.print("지금 저금액을 입력하세요: ");
        // 입력 받기
        int nowSaving = scanner.nextInt();
        // 입력 내용 표지
        System.out.print("매달의 저금액을 입력하세요: ");
        // 입력 받기
        int everySaving = scanner.nextInt();

        // 1년의 저금액 계산
        int totalSaving = everySaving * 12;
        // 1년후의 저금액 계산
        int yearlySaving = nowSaving + totalSaving;
        // 출력
        System.out.println(yearlySaving + "원");

        // close
        scanner.close();
    }
}
