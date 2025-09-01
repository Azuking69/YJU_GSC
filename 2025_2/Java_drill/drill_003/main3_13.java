package Java_drill.drill_003;

import java.util.Scanner;

public class main3_13 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("정수를 입력하세요: ");
        // 입력 받기
        int num = scanner.nextInt();
        
        // 3의 배수 & 5의 배수 판단
        if (num % 3 == 0 && num % 5 == 0){
            System.out.println("3과 5 양쪽으로 나누어집니다.");
        } else {
            System.out.println("끊을 수 없습니다.");
        }

        // close
        scanner.close();
    }
    
}