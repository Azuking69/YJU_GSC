package Java_drill.drill_003;

import java.util.Scanner;

public class main3_20 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.print("초 수를 입력하세요: ");
        // 입력 받기
        int count = scanner.nextInt();
        
        // 계산
        int outputHour = count / 3600;
        int second = count % 3600;
        int minute = second / 60;
        int outputSecond = second % 60;
        // 출력
        System.out.println(outputHour + "시" + minute + "분" + outputSecond + '초');
    
        // close
        scanner.close();
    }
}
