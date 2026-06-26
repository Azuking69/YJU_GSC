package Java_drill.drill_003;

import java.util.Scanner;

public class main3_24 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.print("정수를 입력하세요: ");
        // 입력 받기
        int num = scanner.nextInt();

        // 0를 설정
        int result = clearMostSignificantBit(num);
        // 출력
        System.out.println(result);

        // close
        scanner.close();
 
    }

    // 제일 왼쪽에 있는 bit를 0으로 바꾸기
    public static int clearMostSignificantBit(int number){
        int mask = 0x7FFFFFF;
        return number & mask;
    }
}
