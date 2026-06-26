package Java_drill.drill_003;

import java.util.Scanner;

public class main3_8 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("정수를 두 개 입력하네요: ");
        // 입력 받기
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        
        // 두 개 정수가 같은 것인지 확인
        if (num1 == num2){
            System.out.println("같은 정수입니다.");
        }else{
            System.out.println("달른 정수입나다.");
        }

        // close
        scanner.close();
    }
}
