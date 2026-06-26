package Java_drill.drill_003;

import java.util.Scanner;

public class main3_9 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("삼각형의 길을 입력하세요: ");
        // 입력 받기
        double num1 = scanner.nextDouble();
        double num2 = scanner.nextDouble();
        double num3 = scanner.nextDouble();
        
        // 삼각형 되는지 확인
        if (num1 + num2 < num3 || num1 + num3 < num2 || num2 + num3 < num1){
            System.out.println("삼각형 아닙니다.");
        } else {
            System.out.println("삼각형입니다.");
        }

        // close
        scanner.close();
    }
}
