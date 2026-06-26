package Java_drill.drill_002;

// import scanner
import java.util.Scanner;

public class main2_4 {
    public static void main(String[] args) {
        // 입력준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("문자열을 입력하세요: ");
        // 문자열 받기
        String input = scanner.nextLine();
        // 문자열 계산
        int length = input.length();
        // 출력
        System.out.println("입력된 문자열의 길은: " + length);
        // close
        scanner.close();
    }
}
