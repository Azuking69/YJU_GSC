package Java_drill.drill_003;

import java.util.Scanner;

public class main3_4 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지(가격)
        System.out.println("가격을 입력하세요: ");
        // 가격 입력 받기
        int price = scanner.nextInt();
        // 입력 내용 표지(개수)
        System.out.println("개수를 입력하세요: ");
        // 개수 입력 받기
        int cut = scanner.nextInt();
        // 계산
        double total = price * cut;
        // 출력
        System.out.println(total + "원");
        // close
        scanner.close();
    }
}
