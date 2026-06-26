package Java_drill.drill_003;

import java.util.Scanner;

public class main3_10 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        // 입력 내용 표지
        System.out.println("문자열 두 개 입력하세요: ");
        // 입력 받기
        String str1 = scanner.nextLine();
        String str2 = scanner.nextLine();
        
        // 문자열 같은지 확인
        if (areStringsEqual(str1, str2)){
            System.out.println("입력된 문자열은 같습니다.");
        } else {
            System.out.println("입력된 문자열은 안 같습니다.");
        }

        // close
        scanner.close();
    }

    // 판단 내용 정의
    public static boolean areStringsEqual(String str1, String str2){
        return str1.equals(str2);
    }
}
