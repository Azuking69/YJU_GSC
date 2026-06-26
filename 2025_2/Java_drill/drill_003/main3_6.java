package Java_drill.drill_003;

import java.util.Scanner;

public class main3_6 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("정수를 입력하세요: ");
        // 입력 받기
        int num = scanner.nextInt();


        // 홀수/작수 판단
        if (num % 2 == 0){
            System.out.println("작수");
        }else{
            System.out.println("홀수");
        }

        // close
        scanner.close();
    }
}
