package Java_drill.drill_003;

import java.util.Scanner;

public class main3_16 {
    public static void main(String[] args){
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("반지름을 입력 하세요: ");
        // 입력 받기
        double num = scanner.nextDouble();
        
        // 원 계산
        double area = num * num * 3.14415;
        // 출력
        System.out.println(area);

        // close
        scanner.close();
    }
}
