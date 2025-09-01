package Java_drill.drill_003;

import java.util.Scanner;

public class main3_15 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("시험 점수를 입력하세요: ");
        // 입력 받기
        int num = scanner.nextInt();
        
        // 70~90 합격 판단
        if (70 <= num && num < 90){
            System.out.println("합격");
        } else {
            System.out.println("불합격");
        }

        // close
        scanner.close();
    }
}
