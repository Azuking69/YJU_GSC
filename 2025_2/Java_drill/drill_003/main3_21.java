package Java_drill.drill_003;

import java.util.Scanner;

public class main3_21 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.print("정수를 입력하새요: ");
        // 입력 받기
        int num = scanner.nextInt();

        // 계산
        int mostRight = num & 1;
        
        // 판단결과에 따라 출력
        if (mostRight == 1){
            System.out.println("제일 오른쪽에 있는 bit는 1입니다.");
        } else {
            System.out.println("제일 오른쪽에 있는 bit는 0입니다.");
        }

        // close
        scanner.close();
    }
}
