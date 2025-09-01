package Java_drill.drill_003;

import java.util.Scanner;

public class main3_11{
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 나이 입력 표지
        System.out.println("나이를 입력하세요: ");
        // 나이 입력 받기
        int age = scanner.nextInt();
        // 명허증 입력 표지
        System.out.println("명허증이 있습니까?(true or false): ");
        // 명허증 입력 받기
        boolean license = scanner.nextBoolean();

        // 명허증이 있을 때 표지
        if (18 <= age && license){
            System.out.println("운정할 수 있습니다.");
        } else {
            System.out.println("운정할 수 없습니다.");
        }

        // close
        scanner.close();
    }
}