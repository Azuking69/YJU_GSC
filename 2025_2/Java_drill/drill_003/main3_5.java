package Java_drill.drill_003;

import java.util.Scanner;

public class main3_5 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("초수를 입력하세요: ");
        // 입력 받기
        int total = scanner.nextInt();
        // 변환
        int hour = total / 3600;
        int seconds = total % 3600;
        int minute = seconds / 60;
        int finalMinute = seconds % 60;
        // 출력
        System.out.println(hour + "시" + minute + "분" + finalMinute + "초");
        // close
        scanner.close();
    }
}
