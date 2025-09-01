package Java_drill.drill_003;

import java.util.Scanner;

public class main3_12 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("진위치를 두 개 입력하세요: ");
        // 입력 받기
        boolean str1 = scanner.nextBoolean();
        boolean str2 = scanner.nextBoolean();

        // 두 개 같은지 판단
        if (str1 && str2){
            System.out.println("양쪽이 참입니다.");
        } else {
            System.out.println("적어도 하나는 참이 아닙니다.");
        }

        // close
        scanner.close();
    }
}
